from flask import render_template, url_for, redirect, request, session, flash
from flask_login import current_user, login_user, logout_user, login_required
from application import app, db
from application.models import Ingredients, Cuisine, Recipes, Quantity, Method, Schedule, Measure, ShoppingList, User
from application.forms import DeleteRecipeForm, AddRecipeForm1, AddRecipeForm2, AddMetaForm, LoginForm, SearchForm, SelectScheduleForm, FinaliseScheduleForm, AmendAmountForm, PostShoppingListForm, RegistrationForm
from datetime import date, datetime
import calendar
import random
from sqlalchemy import func
import smtplib
import os

# this function gets the recipe for each day, filters by day and logged in user id
def get_recipe_for_day(day_number):
    if current_user.is_authenticated:
        id = Schedule.query.filter_by(day_of_the_week = day_number, user_id = current_user.id).first()
        if id is not None:
            day_recipe = Recipes.query.filter_by(id = id.recipe_id).first()
            return day_recipe
        else:
            return Recipes.query.filter_by(id = 1).first()
    else:
        return Recipes.query.filter_by(id = 1).first()

# this function assembles the recipe for each day adding it to a list in order of the days to be used in the layout template
def get_weekly_recipes():
    week = []
    for num in range(5):
         week.append(get_recipe_for_day(num))
    return week

# check if current user already has a schedule set
def check_for_schedule():
    if Schedule.query.filter_by(user_id = current_user.id).first() is None:
        return False
    return True

#this function grabs the recipe for the individual day (filtering by day and user id) to be used in the layour template 
def get_recipe_of_the_day():
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        recipe_of_the_day = "It's the weekend, do your own thing"
    else:
        recipe_of_the_day = Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = datetime.today().weekday(), user_id = current_user.id).first().recipe_id).first().recipe_name
    return recipe_of_the_day

# check if it's a weekend
def weekend_or_not():
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        weekend = True
    else:
        weekend = False
    return weekend

def what_day_is_it():
    day = date.today()
    day = calendar.day_name[day.weekday()]

# this cycles through the shopping list picks out the relevant items (filtered by user id), grabbing the data from other tables and puts it into a list of lists with relevant details. 
def create_shopping_list():
    shopping_list_raw = ShoppingList.query.filter_by(user_id = current_user.id).all()
    shopping_list = []
    for shopping_list_raw_item in shopping_list_raw:
        shopping_list.append([Ingredients.query.filter_by(id=shopping_list_raw_item.ingredient_id).first().ingredient_name, shopping_list_raw_item.amount, Measure.query.filter_by(id = shopping_list_raw_item.measure_id).first().measure])
    return shopping_list

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
@login_required
def index():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "weekend" : weekend_or_not(),
        "day" : what_day_is_it(),
        "user" : current_user.username
        }
    else:
        sidebar = False

    total_number = Recipes.query.count()
    if datetime.today().weekday() in [0,1,2,3,4]:
        daily_recipe = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first()
        cuisine = Cuisine.query.filter_by(id=daily_recipe.cuisine_id).first().cuisine_name
        method_list = [m.step for m in Method.query.filter_by(recipe_id = daily_recipe.id)]
        quantities = Quantity.query.filter_by(recipe_id = daily_recipe.id).all()
        ingredient_list = []
        n = 0
        for q in quantities:
            ingredient_list.append([])
            ingredient_list[n].append(Ingredients.query.filter_by(id = q.ingredient_id).first().ingredient_name)
            ingredient_list[n].append(q.amount)
            ingredient_list[n].append(Measure.query.filter_by(id = q.measure).first().measure)
            ingredient_list[n].append(q.ingredient_prep)
            n += 1
    else:
        daily_recipe = False
        cuisine = False
        method_list = False
        quantities = False
        ingredient_list = False
    return render_template('index.html', daily_recipe=daily_recipe, total_number=total_number, cuisine=cuisine, method_list=method_list, ingredient_list=ingredient_list, sidebar=sidebar)
    
@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, you are now a registered user')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)

@app.route('/create_weekly_schedule', methods = ['GET', 'POST'])
@login_required
def create_weekly_schedule():
    user = current_user.username
    form = SelectScheduleForm()
    choices = [(cuisine.id, cuisine.cuisine_name) for cuisine in Cuisine.query.order_by('cuisine_name')]
    choices.insert(0, ("", ""))
    form.first_cuisine.choices = choices
    form.second_cuisine.choices = choices
    form.third_cuisine.choices = choices
    form.fourth_cuisine.choices = choices
    form.fifth_cuisine.choices = choices

    if request.method == 'POST': 
        first_cuisine_id = form.first_cuisine.data
        second_cuisine_id = form.second_cuisine.data 
        third_cuisine_id = form.third_cuisine.data
        fourth_cuisine_id = form.fourth_cuisine.data
        fifth_cuisine_id = form.fifth_cuisine.data 

    # code below create a list of all recipes in the cuisine selected
        if first_cuisine_id == "":
            first_recipe_list = Recipes.query.all()
        else:
            first_recipe_list = Recipes.query.filter_by(cuisine_id = first_cuisine_id).all()
        
        if second_cuisine_id == "":
            second_recipe_list = Recipes.query.all()
        else:
            second_recipe_list = Recipes.query.filter_by(cuisine_id = second_cuisine_id).all()
        
        if third_cuisine_id == "":
            third_recipe_list = Recipes.query.all()
        else:
            third_recipe_list = Recipes.query.filter_by(cuisine_id = third_cuisine_id).all()

        if fourth_cuisine_id == "":
            fourth_recipe_list = Recipes.query.all()
        else:
            fourth_recipe_list = Recipes.query.filter_by(cuisine_id = fourth_cuisine_id).all()

        if fifth_cuisine_id == "":
            fifth_recipe_list = Recipes.query.all()
        else:
            fifth_recipe_list = Recipes.query.filter_by(cuisine_id = fifth_cuisine_id).all()

        # shuffles lists of recipes and add randomised first in the list to the weekly schedule 
        random.shuffle(first_recipe_list)
        random.shuffle(second_recipe_list)
        random.shuffle(third_recipe_list)
        random.shuffle(fourth_recipe_list)
        random.shuffle(fifth_recipe_list)

        weekly_schedule = []
        weekly_schedule.append(first_recipe_list[0])
        weekly_schedule.append(second_recipe_list[0])
        weekly_schedule.append(third_recipe_list[0])
        weekly_schedule.append(fourth_recipe_list[0])
        weekly_schedule.append(fifth_recipe_list[0])
        random.shuffle(weekly_schedule)
        schedule_day = 0
        if Schedule.query.filter_by(day_of_the_week = schedule_day).first():
            sched_no = 1
        else:
            sched_no = 2
        for recipe in weekly_schedule:
            sched = Schedule.query.filter_by(day_of_the_week = schedule_day).first()
            sched.recipe_id = recipe.id
            sched.user_id = current_user.id
            sched.week = sched_no
            db.session.add(sched)
            db.session.commit()
            schedule_day += 1 
        # get a list of all the ingredient, quantities and units in the weekly schedule
        return redirect(url_for('finalise_schedule'))
    else:
        return render_template('create_weekly_schedule.html', user=user, form=form)

@app.route('/finalise_schedule', methods=['POST','GET'])
@login_required
def finalise_schedule():
    user = current_user.username
    form = FinaliseScheduleForm()
    choices = [(r.id, r.recipe_name) for r in Recipes.query.order_by('recipe_name')]
    choices.insert(0, ("", ""))
    form.monday_recipe.choices = choices
    form.tuesday_recipe.choices = choices
    form.wednesday_recipe.choices = choices
    form.thursday_recipe.choices = choices
    form.friday_recipe.choices = choices
    if request.method == 'POST':
        if form.monday_cb.data == True:
            sched = Schedule.query.filter_by(day_of_the_week = 0).first()
            sched.recipe_id = form.monday_recipe.data
            db.session.add(sched)
            db.session.commit()
        if form.tuesday_cb.data == True:
            sched = Schedule.query.filter_by(day_of_the_week = 1).first()
            sched.recipe_id = form.tuesday_recipe.data
            db.session.add(sched)
            db.session.commit()
        if form.wednesday_cb.data == True:
            sched = Schedule.query.filter_by(day_of_the_week = 2).first()
            sched.recipe_id = form.wednesday_recipe.data
            db.session.add(sched)
            db.session.commit()
        if form.thursday_cb.data == True:
            sched = Schedule.query.filter_by(day_of_the_week = 3).first()
            sched.recipe_id = form.thursday_recipe.data
            db.session.add(sched)
            db.session.commit()
        if form.friday_cb.data == True:
            sched = Schedule.query.filter_by(day_of_the_week = 4).first()
            sched.recipe_id = form.friday_recipe.data
            db.session.add(sched)
            db.session.commit()
        
        monday_recipe_ingredients = Quantity.query.filter_by(recipe_id = (Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id)).all()
        tuesday_recipe_ingredients = Quantity.query.filter_by(recipe_id = (Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id)).all()
        wednesday_recipe_ingredients = Quantity.query.filter_by(recipe_id = (Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id)).all()
        thursday_recipe_ingredients = Quantity.query.filter_by(recipe_id = (Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id)).all()
        friday_recipe_ingredients = Quantity.query.filter_by(recipe_id = (Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id)).all()
        ingredient_list = []
        for m in monday_recipe_ingredients:
            ingredient_list.append([m.ingredient_id, m.amount, m.measure])
        for m in tuesday_recipe_ingredients:
            ingredient_list.append([m.ingredient_id, m.amount, m.measure])
        for m in wednesday_recipe_ingredients:
            ingredient_list.append([m.ingredient_id, m.amount, m.measure])
        for m in thursday_recipe_ingredients:
            ingredient_list.append([m.ingredient_id, m.amount, m.measure])
        for m in friday_recipe_ingredients:
            ingredient_list.append([m.ingredient_id, m.amount, m.measure])
        # ingredient list should now be a list of all ingredients seperated into a list of three elements (ingredients.id, amount, unit) however some are likely to be duplicates. The below code is iterating over the list to add up any duplciates to pass one value to aggregated_ingredient_list
        
        #clears shopping list table
        db.session.query(ShoppingList).delete()
        db.session.commit()

        # this code looks for unique values and adds them to aggregated_ingredient_list
        ingredient_ids = [ingredient[0] for ingredient in ingredient_list]
        unique_ingredients = set(ingredient_ids)
        aggregated_ingredient_list = []
        for ingr in unique_ingredients:
            a = [0,0,0]
            for ing in ingredient_list:
                if ingr == ing[0]:
                    a[0] = ing[0]
                    a[1] += ing[1]
                    a[2] = ing[2]
            shop_item = ShoppingList(a[0], a[1], a[2], current_user.id)
            db.session.add(shop_item)
            db.session.commit()
            aggregated_ingredient_list.append(shop_item)
        return redirect(url_for('amend_shopping_list')) 
    else:
        weekly_schedule = Schedule.query.order_by('day_of_the_week')
        mon = Recipes.query.filter_by(id = weekly_schedule[0].recipe_id).first().recipe_name
        tue = Recipes.query.filter_by(id = weekly_schedule[1].recipe_id).first().recipe_name
        wed = Recipes.query.filter_by(id = weekly_schedule[2].recipe_id).first().recipe_name
        thu = Recipes.query.filter_by(id = weekly_schedule[3].recipe_id).first().recipe_name
        fri = Recipes.query.filter_by(id = weekly_schedule[4].recipe_id).first().recipe_name
        return render_template('finalise_schedule.html', user=user, form=form, mon=mon, tue=tue, wed=wed, thu=thu, fri=fri)

@app.route('/amend_shopping_list', methods = ['GET', 'POST'])
@login_required
def amend_shopping_list():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        "shopping_list" : create_shopping_list(),
        }
    else:
        sidebar = False

    print(sidebar["shopping_list"])
    amount_list = [{i[0] : i[1]} for i in sidebar["shopping_list"]]
    form = AmendAmountForm(ingredients = amount_list)

    if request.method == "POST":
        s = db.session.query(func.min(ShoppingList.id)).first()
        n = s[0]
        for ingr in form.ingredients.data:
            sl = ShoppingList.query.filter_by(id = n).first()
            if ingr["amount"] == None:
                pass
            elif ingr["amount"] == 0:
                db.session.delete(sl)
                db.session.commit()
            else:
                 sl.amount = ingr["amount"]
                 db.session.commit()
            n += 1   
        return redirect(url_for("post_shopping_list"))
    else:
        return render_template('amend_shopping_list.html', sidebar = sidebar, form=form)

@app.route('/post_shopping_list', methods = ['GET', 'POST'])
@login_required
def post_shopping_list():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        "shopping_list" : create_shopping_list(),
        }
    else:
        sidebar = False

    form = PostShoppingListForm()
    if request.method == "POST":
        gmail_user = "recipeapp909@gmail.com"
        gmail_password = os.environ['GMAIL']
        print(os.environ['GMAIL'])
        sent_from = gmail_user
        email_input = form.email.data
        to = [current_user.email, email_input]
        subject = 'Ingredient list for weekly recipes'
        body =  "Weekly Shopping List\n\n"
        for ingredient in sidebar["shopping_list"]:
            body += f"{ingredient[0]} {ingredient[1]} {ingredient[2]}\n"
        email_text= "from:{}\nto:{}\nsubject:{}\n{}".format(sent_from, ",".join(to),subject,body)
        try:
            smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user,gmail_password)
            smtp_server.sendmail(sent_from,to,email_text)
            smtp_server.close()
            message = "Email sent Successfully"
        except Exception as ex:
            message = f"Something went wrong..... +{ex}"
        return render_template("post_shopping_list.html", sidebar = sidebar, form=form, message=message)
    else:
        return render_template("post_shopping_list.html", sidebar = sidebar, form=form)

@app.route('/search_recipes', methods = ['GET', 'POST'])
@login_required
def search_recipes():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        }
    else:
        sidebar = False

    form = SearchForm()
    form.recipe.choices = [(r.id, r.recipe_name) for r in Recipes.query.order_by('recipe_name')]
    total_number = Recipes.query.count()

    if request.method == 'POST':
        recipe_result = Recipes.query.filter_by(id=form.recipe.data).first()
        cuisine = Cuisine.query.filter_by(id=recipe_result.cuisine_id).first().cuisine_name
        method_list = [m.step for m in Method.query.filter_by(recipe_id = recipe_result.id)]
        quantities = Quantity.query.filter_by(recipe_id = recipe_result.id).all()
        ingredient_list = []
        n = 0
        for q in quantities:
            ingredient_list.append([])
            ingredient_list[n].append(Ingredients.query.filter_by(id = q.ingredient_id).first().ingredient_name)
            ingredient_list[n].append(q.amount)
            ingredient_list[n].append(Measure.query.filter_by(id = q.measure).first().measure)
            ingredient_list[n].append(q.ingredient_prep)
            n += 1
        return render_template('search.html', sidebar = sidebar, form=form, total_number=total_number, recipe_result=recipe_result, cuisine=cuisine, method_list=method_list, ingredient_list=ingredient_list)
    else:
        return render_template('search.html', sidebar = sidebar, form=form, total_number=total_number)
  
@app.route('/add_meta', methods = ['GET', 'POST'])
@login_required
def add_meta():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        }
    else:
        sidebar = False

    form = AddMetaForm()
    if request.method == 'POST':
        ingredient = form.ingredient.data

        cuisine = form.cuisine.data
        measure = form.measure.data
        if ingredient != "":
            ing = Ingredients(ingredient)
            db.session.add(ing)
            db.session.commit()
        if cuisine != "":
            cus = Cuisine(cuisine)
            db.session.add(cus)
            db.session.commit()
        if measure != "":
            meas = Measure(measure)
            db.session.add(meas)
            db.session.commit()
        return render_template('add_meta.html', sidebar = sidebar, ingredient = ingredient, cuisine=cuisine, form=form, measure=measure)
    else:
        return render_template('add_meta.html', sidebar = sidebar, form=form)

@app.route('/delete_recipe', methods= ['GET', 'POST'])
@login_required
def delete_recipe():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        }
    else:
        sidebar = False
    
    form = DeleteRecipeForm()
    if request.method == 'POST':
        form.recipe.choices = [(r.id, r.recipe_name) for r in Recipes.query.order_by('recipe_name')]
        recipe_to_delete = Recipes.query.filter_by(id = form.recipe.data).first()
        quantities_to_delete = Quantity.query.filter_by(recipe_id = recipe_to_delete.id).all()
        for q in quantities_to_delete:
            db.session.delete(q)
            db.session.commit()
        methods_to_delete = Method.query.filter_by(recipe_id = recipe_to_delete.id).all()
        for m in methods_to_delete:
            db.session.delete(m)
            db.session.commit()
        db.session.delete(recipe_to_delete)
        db.session.commit()
        deleted = True
        return render_template('delete_recipe.html', sidebar = sidebar, form=form, deleted=deleted)
    else:
        form.recipe.choices = [(r.id, r.recipe_name) for r in Recipes.query.order_by('recipe_name')]
        return render_template('delete_recipe.html', sidebar = sidebar, form=form)

@app.route('/add_recipe', methods = ['GET', 'POST'])
@login_required
def add_recipe():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        }
    else:
        sidebar = False

    duplicate = True
    form = AddRecipeForm1()
    form.cuisine.choices = [(c.id, c.cuisine_name) for c in Cuisine.query.order_by('cuisine_name')]
    form.cuisine.choices.insert(0,("",""))

    if request.method == 'POST':
        recipe_name = form.name.data
        recipe_description = form.recipe_description.data
        session['no_ingredients'] = form.no_ingredients.data
        session['no_method_steps'] = form.no_method_steps.data
        if form.cuisine.data == "":
            cuisine = 1
        else:
            cuisine = form.cuisine.data
        recipe = Recipes(recipe_name, recipe_description, cuisine)
        if Recipes.query.filter(Recipes.recipe_name == recipe_name).first():
            return render_template('add_recipe.html', duplicate=duplicate, sidebar = sidebar)
        else:
            db.session.add(recipe)
            db.session.commit()
            session['recipe_id'] = recipe.id
            session['recipe_name'] = recipe.recipe_name
        return redirect(url_for('add_recipe2'))
    else:
        return render_template('add_recipe.html', sidebar = sidebar, form=form) 
        
@app.route('/add_recipe2', methods = ['GET', 'POST'])
@login_required
def add_recipe2():
    if check_for_schedule():
        sidebar = {
        "week" : get_weekly_recipes(),
        "recipe_of_the_day" : get_recipe_of_the_day(),
        "day" : what_day_is_it(),
        "user" : current_user.username,
        }
    else:
        sidebar = False

    no_ingredients = session.get('no_ingredients', None)
    no_method_steps = session.get('no_method_steps', None)
    recipe_id = session.get('recipe_id', None)
    recipe_name = session.get('recipe_name', None)
    form = AddRecipeForm2(ingredients = range(no_ingredients), methods = (range(no_method_steps)))


    choices1 = [(m.id, m.measure) for m in Measure.query.order_by('measure')]
    choices1.insert(0,("",""))
    choices = [(i.id, i.ingredient_name) for i in Ingredients.query.order_by('ingredient_name')]
    choices.insert(0, ("", ""))

    for sub_form in form.ingredients:
        sub_form.ingredient.choices = choices
    for sub_form in form.ingredients:
        sub_form.measure.choices = choices1

    if request.method == 'POST':
        done = True
        # this block of code gets the data from the ingredients filed list, which is a list of dictionaries, each dictionary has the key:value pairs as defined by the class in forms.py. It iterates through the dictionaries building a list of lists, which is then in turn iterated through adding each to the database as a quantity object.
        all_ingredients = []
        ingredient_names = [ingredient.ingredient_name for ingredient in Ingredients.query.all()]
        n = 0
        for ing in form.ingredients.data:
            if ing["ingredient_alt"] == "" and ing["ingredient"] == "":
                    pass
            elif ing["ingredient_alt"] == "" and ing["ingredient"] != "":
                all_ingredients.append([])
                all_ingredients[n].append(recipe_id)
                all_ingredients[n].append(ing["ingredient"])
                all_ingredients[n].append(ing["ingredient_prep"])
                all_ingredients[n].append(ing["amount"])
                all_ingredients[n].append(ing["measure"])
                n += 1
            elif ing["ingredient_alt"] != "" and ing["ingredient_alt"] in ingredient_names:
                all_ingredients.append([])
                all_ingredients[n].append(recipe_id)
                all_ingredients[n].append(Ingredients.query.filter_by(ingredient_name = ing["ingredient_alt"]).first().id)
                all_ingredients[n].append(ing["ingredient_prep"])
                all_ingredients[n].append(ing["amount"])
                all_ingredients[n].append(ing["measure"])
                n += 1
            elif ing["ingredient_alt"] != "" and ing["ingredient_alt"] not in ingredient_names:
                new_ing = Ingredients(ing["ingredient_alt"])
                db.session.add(new_ing)
                db.session.commit()
                all_ingredients.append([])
                all_ingredients[n].append(recipe_id)
                all_ingredients[n].append(new_ing.id)
                all_ingredients[n].append(ing["ingredient_prep"])
                all_ingredients[n].append(ing["amount"])
                all_ingredients[n].append(ing["measure"])
                n += 1
        for i in all_ingredients:
            quant = Quantity(i[0], i[1], i[2], i[3], i[4])
            db.session.add(quant)
            db.session.commit()
        #  This code interates over the methods data dictionary pulling out the "method" value and then adding that to the adatabse with the recipe id and a step number which is incremeneted.
        i = 1
        for meth in form.methods.data:
            if meth["method"] == "":
                pass
            else:
                method_step = Method(recipe_id,i, meth["method"])
                i += 1
            db.session.add(method_step)
            db.session.commit()

        return render_template('add_recipe2.html', sidebar = sidebar, done=done)
    else:
        return render_template('add_recipe2.html', sidebar = sidebar, form=form, recipe=recipe_name)  
                