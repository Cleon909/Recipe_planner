from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Ingredients, Cuisine, Recipes, Quantity, Method, Schedule, Measure, ShoppingList
from application.forms import AddRecipeForm, AddMetaForm, SearchForm, SelectScheduleForm, FinaliseScheduleForm
from datetime import date, datetime
import calendar
import random


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
        # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())

    day = date.today()
    day = calendar.day_name[day.weekday()]

    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.
    total_number = Recipes.query.count()
    daily_recipe = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first()
    cuisine = Cuisine.query.filter_by(id=daily_recipe.cuisine_id).first().cuisine_name
    method_list = [m.step for m in Method.query.filter_by(recipe_id = daily_recipe.id)]
    quantities = Quantity.query.filter_by(recipe_id = daily_recipe.id).all()
    print(quantities)
    ingredient_list = []
    n = 0
    for q in quantities:
        ingredient_list.append([])
        ingredient_list[n].append(Ingredients.query.filter_by(id = q.ingredient_id).first().ingredient_name)
        ingredient_list[n].append(q.amount)
        ingredient_list[n].append(Measure.query.filter_by(id = q.measure).first().measure)
        ingredient_list[n].append(q.ingredient_prep)
        n += 1
    return render_template('index.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week, daily_recipe=daily_recipe, total_number=total_number, cuisine=cuisine, method_list=method_list, ingredient_list=ingredient_list)
     


@app.route('/create_weekly_schedule', methods = ['GET', 'POST'])
def create_weekly_schedule():
    # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())

    day = date.today()
    day = calendar.day_name[day.weekday()]

    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.
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
        for recipe in weekly_schedule:
            sched = Schedule.query.filter_by(day_of_the_week = schedule_day).first()
            sched.recipe_id = recipe.id
            db.session.add(sched)
            db.session.commit()
            schedule_day += 1 
        # get a list of all the ingredient, quantities and units in the weekly schedule
        

        
        return redirect(url_for('finalise_schedule'))
    else:
        return render_template('create_weekly_schedule.html', day=day, week=week, recipe_of_the_day=recipe_of_the_day, form=form)

@app.route('/finalise_schedule', methods=['POST','GET'])
def finalise_schedule():
    # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())

    day = date.today()
    day = calendar.day_name[day.weekday()]

    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.

    done = True
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
            ingredient_list.append([Ingredients.query.filter_by(id = m.ingredient_id).first().ingredient_name, m.amount, Measure.query.filter_by(id = m.measure).first().measure])
        for m in tuesday_recipe_ingredients:
            ingredient_list.append([Ingredients.query.filter_by(id = m.ingredient_id).first().ingredient_name, m.amount, Measure.query.filter_by(id = m.measure).first().measure])
        for m in wednesday_recipe_ingredients:
            ingredient_list.append([Ingredients.query.filter_by(id = m.ingredient_id).first().ingredient_name, m.amount, Measure.query.filter_by(id = m.measure).first().measure])
        for m in thursday_recipe_ingredients:
            ingredient_list.append([Ingredients.query.filter_by(id = m.ingredient_id).first().ingredient_name, m.amount, Measure.query.filter_by(id = m.measure).first().measure])
        for m in friday_recipe_ingredients:
            ingredient_list.append([Ingredients.query.filter_by(id = m.ingredient_id).first().ingredient_name, m.amount, Measure.query.filter_by(id = m.measure).first().measure])
        # ingredient list should now be a list of all ingredients seperated into a list of three elements (ingredient_name, amount, unit) however some are likely to be duplicates. The below code is iterating over the list to add up any duplciates to pass one value to aggregated_ingredient_list
        aggregated_ingredient_list = []
        # this code looks for unique values and adds them to aggregated_ingredient_list
        ingredient_names = [ingredient[0] for ingredient in ingredient_list]
        for ingredient in ingredient_names:
            if ingredient_names.count(ingredient) == 1:
                aggregated_ingredient_list.append(ingredient_list[aggregated_ingredient_list.index(ingredient)])
        else:
            for ing in ingredient_list:
                for item in ingredient_list:
                    if ingredient_list.index(ing) == ingredient_list.index(item):
                        pass
                    elif ing[0] == item[0]:
                         ing[1] += item[1]
            aggregated_ingredient_list.append(ing)
            print(aggregated_ingredient_list)
        db.session.query(ShoppingList).delete()
        db.session.commit()
        for element in aggregated_ingredient_list:
            shop = ShoppingList(*element)
            db.session.add(shop)
            db.session.commit()

        return render_template('finalise_schedule.html', day=day, week=week, recipe_of_the_day=recipe_of_the_day, done=done, aggregated_ingredient_list=aggregated_ingredient_list)
    else:
        weekly_schedule = Schedule.query.order_by('day_of_the_week')
        mon = Recipes.query.filter_by(id = weekly_schedule[0].recipe_id).first().recipe_name
        tue = Recipes.query.filter_by(id = weekly_schedule[1].recipe_id).first().recipe_name
        wed = Recipes.query.filter_by(id = weekly_schedule[2].recipe_id).first().recipe_name
        thu = Recipes.query.filter_by(id = weekly_schedule[3].recipe_id).first().recipe_name
        fri = Recipes.query.filter_by(id = weekly_schedule[4].recipe_id).first().recipe_name
        return render_template('finalise_schedule.html', day=day, week=week, recipe_of_the_day=recipe_of_the_day, form=form, mon=mon, tue=tue, wed=wed, thu=thu, fri=fri)

@app.route('/search_recipes', methods = ['GET', 'POST'])
def search_recipes():
    # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())

    day = date.today()
    day = calendar.day_name[day.weekday()]

    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.    
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
        return render_template('search.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week, form=form, total_number=total_number, recipe_result=recipe_result, cuisine=cuisine, method_list=method_list, ingredient_list=ingredient_list)
    else:
        return render_template('search.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week, form=form, total_number=total_number)
  
@app.route('/add_meta', methods = ['GET', 'POST'])
def add_meta():
    # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())

    day = date.today()
    day = calendar.day_name[day.weekday()]

    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.
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
        return render_template('add_meta.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week, ingredient = ingredient, cuisine=cuisine, form=form, measure=measure)
    else:
        return render_template('add_meta.html', day=day, recipe_of_the_day=recipe_of_the_day, form=form, week=week)


@app.route('/add_recipe', methods = ['GET', 'POST'])
def add_recipe():
    # variables for the layout html template.
    week = []
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 0).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 1).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 2).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 3).first().recipe_id).first())
    week.append(Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = 4).first().recipe_id).first())
    day = date.today()
    day = calendar.day_name[day.weekday()]
    recipe_of_the_day = Recipes.query.filter_by(id = (Schedule.query.filter_by(day_of_the_week = datetime.today().weekday()).first().recipe_id)).first().recipe_name
    # variables for the layout html template.

    duplicate = True
    form = AddRecipeForm()
    form.cuisine.choices = [(c.id, c.cuisine_name) for c in Cuisine.query.order_by('cuisine_name')]
    form.cuisine.choices.insert(0,("",""))
    choices1 = [(m.id, m.measure) for m in Measure.query.order_by('measure')]
    choices1.insert(0,("",""))
    choices = [(i.id, i.ingredient_name) for i in Ingredients.query.order_by('ingredient_name')]
    choices.insert(0, ("", ""))
    form.ingredient1.choices = choices
    form.ingredient2.choices = choices
    form.ingredient3.choices = choices
    form.ingredient4.choices = choices
    form.ingredient5.choices = choices
    form.ingredient6.choices = choices
    form.ingredient7.choices = choices
    form.ingredient8.choices = choices
    form.ingredient9.choices = choices
    form.ingredient10.choices = choices
    form.ingredient11.choices = choices
    form.ingredient12.choices = choices
    form.ingredient13.choices = choices
    form.ingredient14.choices = choices
    form.ingredient15.choices = choices
    form.ingredient16.choices = choices
    form.ingredient17.choices = choices
    form.ingredient18.choices = choices
    form.ingredient19.choices = choices
    form.ingredient20.choices = choices
    form.ingredient21.choices = choices
    form.ingredient22.choices = choices
    form.ingredient23.choices = choices
    form.ingredient24.choices = choices
    form.ingredient25.choices = choices
    form.ingredient26.choices = choices
    form.ingredient27.choices = choices
    form.ingredient28.choices = choices
    form.ingredient29.choices = choices
    form.ingredient30.choices = choices
    form.measure1.choices = choices1
    form.measure2.choices = choices1
    form.measure3.choices = choices1
    form.measure4.choices = choices1
    form.measure5.choices = choices1
    form.measure6.choices = choices1
    form.measure7.choices = choices1
    form.measure8.choices = choices1
    form.measure9.choices = choices1
    form.measure10.choices = choices1
    form.measure11.choices = choices1
    form.measure12.choices = choices1
    form.measure13.choices = choices1
    form.measure14.choices = choices1
    form.measure15.choices = choices1
    form.measure16.choices = choices1
    form.measure16.choices = choices1
    form.measure17.choices = choices1
    form.measure18.choices = choices1
    form.measure19.choices = choices1
    form.measure20.choices = choices1
    form.measure21.choices = choices1
    form.measure22.choices = choices1
    form.measure23.choices = choices1
    form.measure24.choices = choices1
    form.measure25.choices = choices1
    form.measure26.choices = choices1
    form.measure27.choices = choices1
    form.measure28.choices = choices1
    form.measure29.choices = choices1
    form.measure30.choices = choices1

    if request.method == 'POST':
        recipe_name = form.name.data
        recipe_description = form.recipe_description.data
        if form.cuisine.data == "":
            cuisine = 1
        else:
            cuisine = form.cuisine.data
        recipe = Recipes(recipe_name, recipe_description, cuisine)
        if Recipes.query.filter(Recipes.recipe_name == recipe_name).first():
            return render_template('add_recipe.html', duplicate=duplicate)
        else:
            db.session.add(recipe)
            db.session.commit()
        

        all_ingredients = []
        ingredient_names = [ingredient.ingredient_name for ingredient in Ingredients.query.all()]

        if form.ingredient_alt1.data == "":
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(form.ingredient1.data)
            all_ingredients[0].append(form.ingredient_prep1.data)
            all_ingredients[0].append(form.amount1.data)
            all_ingredients[0].append(form.measure1.data)
        elif form.ingredient_alt1.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt1.data).first().id)
            all_ingredients[0].append(form.ingredient_prep1.data)
            all_ingredients[0].append(form.amount1.data)
            all_ingredients[0].append(form.measure1.data)
        else:
            ing = Ingredients(form.ingredient_alt1.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(ing.id)
            all_ingredients[0].append(form.ingredient_prep1.data)
            all_ingredients[0].append(form.amount1.data)
            all_ingredients[0].append(form.measure1.data)

        if form.ingredient_alt2.data == "":
            all_ingredients.append([])
            all_ingredients[1].append(recipe.id)
            all_ingredients[1].append(form.ingredient2.data)
            all_ingredients[1].append(form.ingredient_prep2.data)
            all_ingredients[1].append(form.amount2.data)
            all_ingredients[1].append(form.measure2.data)
        elif form.ingredient_alt2.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt2.data).first().id)
            all_ingredients[0].append(form.ingredient_prep2.data)
            all_ingredients[0].append(form.amount2.data)
            all_ingredients[0].append(form.measure2.data)
        else:
            ing = Ingredients(form.ingredient_alt2.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[1].append(recipe.id)
            all_ingredients[1].append(ing.id)
            all_ingredients[1].append(form.ingredient_prep2.data)
            all_ingredients[1].append(form.amount2.data)
            all_ingredients[1].append(form.measure2.data)
        
        if form.ingredient_alt3.data == "":
            all_ingredients.append([])
            all_ingredients[2].append(recipe.id)
            all_ingredients[2].append(form.ingredient3.data)
            all_ingredients[2].append(form.ingredient_prep3.data)
            all_ingredients[2].append(form.amount3.data)
            all_ingredients[2].append(form.measure3.data)
        elif form.ingredient_alt3.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt3.data).first().id)
            all_ingredients[0].append(form.ingredient_prep3.data)
            all_ingredients[0].append(form.amount3.data)
            all_ingredients[0].append(form.measure3.data)
        else:
            ing = Ingredients(form.ingredient_alt3.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[2].append(recipe.id)
            all_ingredients[2].append(ing.id)
            all_ingredients[2].append(form.ingredient_prep1.data)
            all_ingredients[2].append(form.amount3.data)
            all_ingredients[2].append(form.measure3.data)
        
        if form.ingredient_alt4.data == "":
            all_ingredients.append([])
            all_ingredients[3].append(recipe.id)
            all_ingredients[3].append(form.ingredient4.data)
            all_ingredients[3].append(form.ingredient_prep4.data)
            all_ingredients[3].append(form.amount4.data)
            all_ingredients[3].append(form.measure4.data)
        elif form.ingredient_alt4.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt4.data).first().id)
            all_ingredients[0].append(form.ingredient_prep4.data)
            all_ingredients[0].append(form.amount4.data)
            all_ingredients[0].append(form.measure4.data)
        else:
            ing = Ingredients(form.ingredient_alt4.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[3].append(recipe.id)
            all_ingredients[3].append(ing.id)
            all_ingredients[3].append(form.ingredient_prep4.data)
            all_ingredients[3].append(form.amount4.data)
            all_ingredients[3].append(form.measure4.data)
        
        if form.ingredient_alt5.data == "":
            all_ingredients.append([])
            all_ingredients[4].append(recipe.id)
            all_ingredients[4].append(form.ingredient5.data)
            all_ingredients[4].append(form.ingredient_prep5.data)
            all_ingredients[4].append(form.amount5.data)
            all_ingredients[4].append(form.measure5.data)
        elif form.ingredient_alt5.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt5.data).first().id)
            all_ingredients[0].append(form.ingredient_prep5.data)
            all_ingredients[0].append(form.amount5.data)
            all_ingredients[0].append(form.measure5.data)
        else:
            ing = Ingredients(form.ingredient_alt5.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[4].append(recipe.id)
            all_ingredients[4].append(ing.id)
            all_ingredients[4].append(form.ingredient_prep5.data)
            all_ingredients[4].append(form.amount5.data)
            all_ingredients[4].append(form.measure5.data)
        
        if form.ingredient_alt6.data == "":
            all_ingredients.append([])
            all_ingredients[5].append(recipe.id)
            all_ingredients[5].append(form.ingredient6.data)
            all_ingredients[5].append(form.ingredient_prep6.data)
            all_ingredients[5].append(form.amount6.data)
            all_ingredients[5].append(form.measure6.data)
        elif form.ingredient_alt6.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt6.data).first().id)
            all_ingredients[0].append(form.ingredient_prep6.data)
            all_ingredients[0].append(form.amount6.data)
            all_ingredients[0].append(form.measure6.data)
        else:
            ing = Ingredients(form.ingredient_alt6.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[5].append(recipe.id)
            all_ingredients[5].append(ing.id)
            all_ingredients[5].append(form.ingredient_prep6.data)
            all_ingredients[5].append(form.amount6.data)
            all_ingredients[5].append(form.measure6.data)
        
        if form.ingredient_alt7.data == "":
            all_ingredients.append([])
            all_ingredients[6].append(recipe.id)
            all_ingredients[6].append(form.ingredient7.data)
            all_ingredients[6].append(form.ingredient_prep7.data)
            all_ingredients[6].append(form.amount7.data)
            all_ingredients[6].append(form.measure7.data)
        elif form.ingredient_alt7.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt7.data).first().id)
            all_ingredients[0].append(form.ingredient_prep7.data)
            all_ingredients[0].append(form.amount7.data)
            all_ingredients[0].append(form.measure7.data)
        else:
            ing = Ingredients(form.ingredient_alt7.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[6].append(recipe.id)
            all_ingredients[6].append(ing.id)
            all_ingredients[6].append(form.ingredient_prep7.data)
            all_ingredients[6].append(form.amount7.data)
            all_ingredients[6].append(form.measure7.data)
        
        if form.ingredient_alt8.data == "":
            all_ingredients.append([])
            all_ingredients[7].append(recipe.id)
            all_ingredients[7].append(form.ingredient8.data)
            all_ingredients[7].append(form.ingredient_prep8.data)
            all_ingredients[7].append(form.amount8.data)
            all_ingredients[7].append(form.measure8.data)
        elif form.ingredient_alt8.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt8.data).first().id)
            all_ingredients[0].append(form.ingredient_prep8.data)
            all_ingredients[0].append(form.amount8.data)
            all_ingredients[0].append(form.measure8.data)
        else:
            ing = Ingredients(form.ingredient_alt8.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[7].append(recipe.id)
            all_ingredients[7].append(ing.id)
            all_ingredients[7].append(form.ingredient_prep8.data)
            all_ingredients[7].append(form.amount8.data)
            all_ingredients[7].append(form.measure8.data)
        
        if form.ingredient_alt9.data == "":
            all_ingredients.append([])
            all_ingredients[8].append(recipe.id)
            all_ingredients[8].append(form.ingredient9.data)
            all_ingredients[8].append(form.ingredient_prep9.data)
            all_ingredients[8].append(form.amount9.data)
            all_ingredients[8].append(form.measure9.data)
        elif form.ingredient_alt9.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt9.data).first().id)
            all_ingredients[0].append(form.ingredient_prep9.data)
            all_ingredients[0].append(form.amount9.data)
            all_ingredients[0].append(form.measure9.data)
        else:
            ing = Ingredients(form.ingredient_alt9.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[8].append(recipe.id)
            all_ingredients[8].append(ing.id)
            all_ingredients[8].append(form.ingredient_prep9.data)
            all_ingredients[8].append(form.amount9.data)
            all_ingredients[8].append(form.measure9.data)
        
        if form.ingredient_alt10.data == "":
            all_ingredients.append([])
            all_ingredients[9].append(recipe.id)
            all_ingredients[9].append(form.ingredient10.data)
            all_ingredients[9].append(form.ingredient_prep1.data)
            all_ingredients[9].append(form.amount10.data)
            all_ingredients[9].append(form.measure10.data)
        elif form.ingredient_alt10.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt10.data).first().id)
            all_ingredients[0].append(form.ingredient_prep10.data)
            all_ingredients[0].append(form.amount10.data)
            all_ingredients[0].append(form.measure10.data)
        else:
            ing = Ingredients(form.ingredient_alt10.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[9].append(recipe.id)
            all_ingredients[9].append(ing.id)
            all_ingredients[9].append(form.ingredient_prep10.data)
            all_ingredients[9].append(form.amount10.data)
            all_ingredients[9].append(form.measure10.data)

        if form.ingredient_alt11.data == "":
            all_ingredients.append([])
            all_ingredients[10].append(recipe.id)
            all_ingredients[10].append(form.ingredient11.data)
            all_ingredients[10].append(form.ingredient_prep1.data)
            all_ingredients[10].append(form.amount11.data)
            all_ingredients[10].append(form.measure11.data)
        elif form.ingredient_alt11.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt11.data).first().id)
            all_ingredients[0].append(form.ingredient_prep11.data)
            all_ingredients[0].append(form.amount11.data)
            all_ingredients[0].append(form.measure11.data)
        else:
            ing = Ingredients(form.ingredient_alt1.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[10].append(recipe.id)
            all_ingredients[10].append(ing.id)
            all_ingredients[10].append(form.ingredient_prep11.data)
            all_ingredients[10].append(form.amount11.data)
            all_ingredients[10].append(form.measure11.data)

        if form.ingredient_alt12.data == "":
            all_ingredients.append([])
            all_ingredients[11].append(recipe.id)
            all_ingredients[11].append(form.ingredient12.data)
            all_ingredients[11].append(form.ingredient_prep12.data)
            all_ingredients[11].append(form.amount12.data)
            all_ingredients[11].append(form.measure12.data)
        elif form.ingredient_alt12.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt12.data).first().id)
            all_ingredients[0].append(form.ingredient_prep12.data)
            all_ingredients[0].append(form.amount12.data)
            all_ingredients[0].append(form.measure12.data)
        else:
            ing = Ingredients(form.ingredient_alt12.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[11].append(recipe.id)
            all_ingredients[11].append(ing.id)
            all_ingredients[11].append(form.ingredient_prep12.data)
            all_ingredients[11].append(form.amount12.data)
            all_ingredients[11].append(form.measure12.data)

        if form.ingredient_alt13.data == "":
            all_ingredients.append([])
            all_ingredients[12].append(recipe.id)
            all_ingredients[12].append(form.ingredient13.data)
            all_ingredients[12].append(form.ingredient_prep13.data)
            all_ingredients[12].append(form.amount13.data)
            all_ingredients[12].append(form.measure13.data)
        elif form.ingredient_alt13.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt13.data).first().id)
            all_ingredients[0].append(form.ingredient_prep13.data)
            all_ingredients[0].append(form.amount13.data)
            all_ingredients[0].append(form.measure13.data)
        else:
            ing = Ingredients(form.ingredient_alt13.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[12].append(recipe.id)
            all_ingredients[12].append(ing.id)
            all_ingredients[12].append(form.ingredient_prep13.data)
            all_ingredients[12].append(form.amount13.data)
            all_ingredients[12].append(form.measure13.data)

        if form.ingredient_alt14.data == "":
            all_ingredients.append([])
            all_ingredients[13].append(recipe.id)
            all_ingredients[13].append(form.ingredient14.data)
            all_ingredients[13].append(form.ingredient_prep14.data)
            all_ingredients[13].append(form.amount14.data)
            all_ingredients[13].append(form.measure14.data)
        elif form.ingredient_alt14.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt14.data).first().id)
            all_ingredients[0].append(form.ingredient_prep14.data)
            all_ingredients[0].append(form.amount14.data)
            all_ingredients[0].append(form.measure14.data)
        else:
            ing = Ingredients(form.ingredient_alt14.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[13].append(recipe.id)
            all_ingredients[13].append(ing.id)
            all_ingredients[13].append(form.ingredient_prep14.data)
            all_ingredients[13].append(form.amount14.data)
            all_ingredients[13].append(form.measure14.data)

        if form.ingredient_alt15.data == "":
            all_ingredients.append([])
            all_ingredients[14].append(recipe.id)
            all_ingredients[14].append(form.ingredient15.data)
            all_ingredients[14].append(form.ingredient_prep15.data)
            all_ingredients[14].append(form.amount15.data)
            all_ingredients[14].append(form.measure15.data)
        elif form.ingredient_alt15.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt15.data).first().id)
            all_ingredients[0].append(form.ingredient_prep15.data)
            all_ingredients[0].append(form.amount15.data)
            all_ingredients[0].append(form.measure15.data)
        else:
            ing = Ingredients(form.ingredient_alt15.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[14].append(recipe.id)
            all_ingredients[14].append(ing.id)
            all_ingredients[14].append(form.ingredient_prep15.data)
            all_ingredients[14].append(form.amount15.data)
            all_ingredients[14].append(form.measure15.data)

        if form.ingredient_alt16.data == "":
            all_ingredients.append([])
            all_ingredients[15].append(recipe.id)
            all_ingredients[15].append(form.ingredient16.data)
            all_ingredients[15].append(form.ingredient_prep16.data)
            all_ingredients[15].append(form.amount16.data)
            all_ingredients[15].append(form.measure16.data)
        elif form.ingredient_alt16.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt16.data).first().id)
            all_ingredients[0].append(form.ingredient_prep16.data)
            all_ingredients[0].append(form.amount16.data)
            all_ingredients[0].append(form.measure16.data)
        else:
            ing = Ingredients(form.ingredient_alt16.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[15].append(recipe.id)
            all_ingredients[15].append(ing.id)
            all_ingredients[15].append(form.ingredient_prep16.data)
            all_ingredients[15].append(form.amount16.data)
            all_ingredients[15].append(form.measure16.data)

        if form.ingredient_alt17.data == "":
            all_ingredients.append([])
            all_ingredients[16].append(recipe.id)
            all_ingredients[16].append(form.ingredient17.data)
            all_ingredients[16].append(form.ingredient_prep17.data)
            all_ingredients[16].append(form.amount17.data)
            all_ingredients[16].append(form.measure17.data)
        elif form.ingredient_alt17.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt17.data).first().id)
            all_ingredients[0].append(form.ingredient_prep17.data)
            all_ingredients[0].append(form.amount17.data)
            all_ingredients[0].append(form.measure17.data)
        else:
            ing = Ingredients(form.ingredient_alt17.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[16].append(recipe.id)
            all_ingredients[16].append(ing.id)
            all_ingredients[16].append(form.ingredient_prep17.data)
            all_ingredients[16].append(form.amount17.data)
            all_ingredients[16].append(form.measure17.data)

        if form.ingredient_alt18.data == "":
            all_ingredients.append([])
            all_ingredients[17].append(recipe.id)
            all_ingredients[17].append(form.ingredient18.data)
            all_ingredients[17].append(form.ingredient_prep18.data)
            all_ingredients[17].append(form.amount18.data)
            all_ingredients[17].append(form.measure18.data)
        elif form.ingredient_alt18.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt18.data).first().id)
            all_ingredients[0].append(form.ingredient_prep18.data)
            all_ingredients[0].append(form.amount18.data)
            all_ingredients[0].append(form.measure18.data)
        else:
            ing = Ingredients(form.ingredient_alt18.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[17].append(recipe.id)
            all_ingredients[17].append(ing.id)
            all_ingredients[17].append(form.ingredient_prep18.data)
            all_ingredients[17].append(form.amount18.data)
            all_ingredients[17].append(form.measure18.data)

        if form.ingredient_alt19.data == "":
            all_ingredients.append([])
            all_ingredients[18].append(recipe.id)
            all_ingredients[18].append(form.ingredient19.data)
            all_ingredients[18].append(form.ingredient_prep19.data)
            all_ingredients[18].append(form.amount19.data)
            all_ingredients[18].append(form.measure19.data)
        elif form.ingredient_alt19.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt19.data).first().id)
            all_ingredients[0].append(form.ingredient_prep19.data)
            all_ingredients[0].append(form.amount19.data)
            all_ingredients[0].append(form.measure19.data)
        else:
            ing = Ingredients(form.ingredient_alt19.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[18].append(recipe.id)
            all_ingredients[18].append(ing.id)
            all_ingredients[18].append(form.ingredient_prep19.data)
            all_ingredients[18].append(form.amount19.data)
            all_ingredients[18].append(form.measure19.data)

        if form.ingredient_alt20.data == "":
            all_ingredients.append([])
            all_ingredients[19].append(recipe.id)
            all_ingredients[19].append(form.ingredient20.data)
            all_ingredients[19].append(form.ingredient_prep20.data)
            all_ingredients[19].append(form.amount20.data)
            all_ingredients[19].append(form.measure20.data)
        elif form.ingredient_alt20.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt20.data).first().id)
            all_ingredients[0].append(form.ingredient_prep20.data)
            all_ingredients[0].append(form.amount20.data)
            all_ingredients[0].append(form.measure20.data)
        else:
            ing = Ingredients(form.ingredient_alt20.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[19].append(recipe.id)
            all_ingredients[19].append(ing.id)
            all_ingredients[19].append(form.ingredient_prep20.data)
            all_ingredients[19].append(form.amount20.data)
            all_ingredients[19].append(form.measure20.data)

        if form.ingredient_alt21.data == "":
            all_ingredients.append([])
            all_ingredients[20].append(recipe.id)
            all_ingredients[20].append(form.ingredient21.data)
            all_ingredients[20].append(form.ingredient_prep21.data)
            all_ingredients[20].append(form.amount21.data)
            all_ingredients[20].append(form.measure21.data)
        elif form.ingredient_alt21.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt21.data).first().id)
            all_ingredients[0].append(form.ingredient_prep21.data)
            all_ingredients[0].append(form.amount21.data)
            all_ingredients[0].append(form.measure21.data)
        else:
            ing = Ingredients(form.ingredient_alt21.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[20].append(recipe.id)
            all_ingredients[20].append(ing.id)
            all_ingredients[20].append(form.ingredient_prep21.data)
            all_ingredients[20].append(form.amount21.data)
            all_ingredients[20].append(form.measure21.data)

        
        if form.ingredient_alt22.data == "":
            all_ingredients.append([])
            all_ingredients[21].append(recipe.id)
            all_ingredients[21].append(form.ingredient22.data)
            all_ingredients[21].append(form.ingredient_prep22.data)
            all_ingredients[21].append(form.amount22.data)
            all_ingredients[21].append(form.measure22.data)
        elif form.ingredient_alt22.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt22.data).first().id)
            all_ingredients[0].append(form.ingredient_prep22.data)
            all_ingredients[0].append(form.amount22.data)
            all_ingredients[0].append(form.measure22.data)
        else:
            ing = Ingredients(form.ingredient_alt22.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[21].append(recipe.id)
            all_ingredients[21].append(ing.id)
            all_ingredients[21].append(form.ingredient_prep22.data)
            all_ingredients[21].append(form.amount22.data)
            all_ingredients[21].append(form.measure22.data)

        if form.ingredient_alt23.data == "":
            all_ingredients.append([])
            all_ingredients[22].append(recipe.id)
            all_ingredients[22].append(form.ingredient23.data)
            all_ingredients[22].append(form.ingredient_prep23.data)
            all_ingredients[22].append(form.amount23.data)
            all_ingredients[22].append(form.measure23.data)
        elif form.ingredient_alt23.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt23.data).first().id)
            all_ingredients[0].append(form.ingredient_prep23.data)
            all_ingredients[0].append(form.amount23.data)
            all_ingredients[0].append(form.measure23.data)
        else:
            ing = Ingredients(form.ingredient_alt23.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[22].append(recipe.id)
            all_ingredients[22].append(ing.id)
            all_ingredients[22].append(form.ingredient_prep23.data)
            all_ingredients[22].append(form.amount23.data)
            all_ingredients[22].append(form.measure23.data)

        if form.ingredient_alt24.data == "":
            all_ingredients.append([])
            all_ingredients[23].append(recipe.id)
            all_ingredients[23].append(form.ingredient24.data)
            all_ingredients[23].append(form.ingredient_prep24.data)
            all_ingredients[23].append(form.amount24.data)
            all_ingredients[23].append(form.measure24.data)
        elif form.ingredient_alt24.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt24.data).first().id)
            all_ingredients[0].append(form.ingredient_prep24.data)
            all_ingredients[0].append(form.amount24.data)
            all_ingredients[0].append(form.measure24.data)
        else:
            ing = Ingredients(form.ingredient_alt24.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[23].append(recipe.id)
            all_ingredients[23].append(ing.id)
            all_ingredients[23].append(form.ingredient_prep24.data)
            all_ingredients[23].append(form.amount24.data)
            all_ingredients[23].append(form.measure24.data)

        if form.ingredient_alt25.data == "":
            all_ingredients.append([])
            all_ingredients[24].append(recipe.id)
            all_ingredients[24].append(form.ingredient25.data)
            all_ingredients[24].append(form.ingredient_prep25.data)
            all_ingredients[24].append(form.amount25.data)
            all_ingredients[24].append(form.measure25.data)
        elif form.ingredient_alt25.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt25.data).first().id)
            all_ingredients[0].append(form.ingredient_prep25.data)
            all_ingredients[0].append(form.amount25.data)
            all_ingredients[0].append(form.measure25.data)
        else:
            ing = Ingredients(form.ingredient_alt25.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[24].append(recipe.id)
            all_ingredients[24].append(ing.id)
            all_ingredients[24].append(form.ingredient_prep25.data)
            all_ingredients[24].append(form.amount25.data)
            all_ingredients[24].append(form.measure25.data)

        if form.ingredient_alt26.data == "":
            all_ingredients.append([])
            all_ingredients[25].append(recipe.id)
            all_ingredients[25].append(form.ingredient26.data)
            all_ingredients[25].append(form.ingredient_prep26.data)
            all_ingredients[25].append(form.amount26.data)
            all_ingredients[25].append(form.measure26.data)
        elif form.ingredient_alt26.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt26.data).first().id)
            all_ingredients[0].append(form.ingredient_prep26.data)
            all_ingredients[0].append(form.amount26.data)
            all_ingredients[0].append(form.measure26.data)
        else:
            ing = Ingredients(form.ingredient_alt26.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[25].append(recipe.id)
            all_ingredients[25].append(ing.id)
            all_ingredients[25].append(form.ingredient_prep26.data)
            all_ingredients[25].append(form.amount26.data)
            all_ingredients[25].append(form.measure26.data)

        if form.ingredient_alt27.data == "":
            all_ingredients.append([])
            all_ingredients[26].append(recipe.id)
            all_ingredients[26].append(form.ingredient27.data)
            all_ingredients[26].append(form.ingredient_prep27.data)
            all_ingredients[26].append(form.amount27.data)
            all_ingredients[26].append(form.measure27.data)
        elif form.ingredient_alt27.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt27.data).first().id)
            all_ingredients[0].append(form.ingredient_prep27.data)
            all_ingredients[0].append(form.amount27.data)
            all_ingredients[0].append(form.measure27.data)
        else:
            ing = Ingredients(form.ingredient_alt27.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[26].append(recipe.id)
            all_ingredients[26].append(ing.id)
            all_ingredients[26].append(form.ingredient_prep27.data)
            all_ingredients[26].append(form.amount27.data)
            all_ingredients[26].append(form.measure27.data)

        if form.ingredient_alt28.data == "":
            all_ingredients.append([])
            all_ingredients[27].append(recipe.id)
            all_ingredients[27].append(form.ingredient28.data)
            all_ingredients[27].append(form.ingredient_prep28.data)
            all_ingredients[27].append(form.amount28.data)
            all_ingredients[27].append(form.measure28.data)
        elif form.ingredient_alt28.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt28.data).first().id)
            all_ingredients[0].append(form.ingredient_prep28.data)
            all_ingredients[0].append(form.amount28.data)
            all_ingredients[0].append(form.measure28.data)
        else:
            ing = Ingredients(form.ingredient_alt28.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[27].append(recipe.id)
            all_ingredients[27].append(ing.id)
            all_ingredients[27].append(form.ingredient_prep28.data)
            all_ingredients[27].append(form.amount28.data)
            all_ingredients[27].append(form.measure28.data)

        if form.ingredient_alt29.data == "":
            all_ingredients.append([])
            all_ingredients[28].append(recipe.id)
            all_ingredients[28].append(form.ingredient29.data)
            all_ingredients[28].append(form.ingredient_prep29.data)
            all_ingredients[28].append(form.amount29.data)
            all_ingredients[28].append(form.measure29.data)
        elif form.ingredient_alt29.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt29.data).first().id)
            all_ingredients[0].append(form.ingredient_prep29.data)
            all_ingredients[0].append(form.amount29.data)
            all_ingredients[0].append(form.measure29.data)
        else:
            ing = Ingredients(form.ingredient_alt29.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[28].append(recipe.id)
            all_ingredients[28].append(ing.id)
            all_ingredients[28].append(form.ingredient_prep29.data)
            all_ingredients[28].append(form.amount29.data)
            all_ingredients[28].append(form.measure29.data)

        if form.ingredient_alt30.data == "":
            all_ingredients.append([])
            all_ingredients[29].append(recipe.id)
            all_ingredients[29].append(form.ingredient30.data)
            all_ingredients[29].append(form.ingredient_prep30.data)
            all_ingredients[29].append(form.amount30.data)
            all_ingredients[29].append(form.measure30.data)
        elif form.ingredient_alt30.data in ingredient_names:
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(Ingredients.query.filter_by(ingredient_name = form.ingredient_alt30.data).first().id)
            all_ingredients[0].append(form.ingredient_prep30.data)
            all_ingredients[0].append(form.amount30.data)
            all_ingredients[0].append(form.measure30.data)
        else:
            ing = Ingredients(form.ingredient_alt30.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[29].append(recipe.id)
            all_ingredients[29].append(ing.id)
            all_ingredients[29].append(form.ingredient_prep30.data)
            all_ingredients[29].append(form.amount30.data)
            all_ingredients[29].append(form.measure30.data)

        for i in all_ingredients:
            if i[3] != None:
                quant = Quantity(i[0], i[1], i[2], i[3], i[4])
                db.session.add(quant)
                db.session.commit()
                all_ingredients = []
            else:
                continue

        method_steps = [form.method1.data, form.method2.data, form.method3.data, form.method4.data, form.method5.data, form.method6.data, form.method7.data, form.method8.data, form.method9.data, form.method10.data, form.method11.data, form.method12.data, form.method13.data, form.method14.data, form.method15.data]

        for s in method_steps:
            if s == "":
                continue
            else:
                step = Method(recipe.id, method_steps.index(s)+1,s)
                db.session.add(step)
                db.session.commit()
    
        return render_template('add_recipe.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week, recipe = recipe)
    else:
        return render_template('add_recipe.html', day=day, recipe_of_the_day=recipe_of_the_day, week=week,form=form)