from asyncio.windows_events import NULL
from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Ingredients, Cuisine, Recipes, Quantity, Method
from application.forms import AddRecipeForm
from sqlalchemy.exc import IntegrityError

@app.route('/', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def index():
    return "what"
    # code here for search need to add form and html






@app.route('/add_recipe', methods = ['GET', 'POST'])
def add_recipe():
    duplicate = True
    form = AddRecipeForm()
    form.cuisine.choices = [(c.id, c.cuisine_name) for c in Cuisine.query.order_by('cuisine_name')]
    form.cuisine.choices.insert(0,("",""))
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
    

    if request.method == 'POST':
        recipe_name = form.name.data
        recipe_description = form.recipe_description.data
        cuisine = form.cuisine.data
        recipe = Recipes(recipe_name, recipe_description, cuisine)
        if Recipes.query.filter(Recipes.recipe_name == recipe_name).first():
            return render_template('add_recipe.html', duplicate=duplicate)
        else:
            db.session.add(recipe)
            db.session.commit()
        

        all_ingredients = []

        if form.ingredient_alt1.data == "":
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(form.ingredient1.id)
            all_ingredients[0].append(form.ingredient_prep1.data)
            all_ingredients[0].append(form.amount1.data)
            all_ingredients[0].append(form.unit1.data)
        else:
            ing = Ingredients(form.ingredient_alt1.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[0].append(recipe.id)
            all_ingredients[0].append(ing.id)
            all_ingredients[0].append(form.ingredient_prep1.data)
            all_ingredients[0].append(form.amount1.data)
            all_ingredients[0].append(form.unit1.data)

        if form.ingredient_alt2.data == "":
            all_ingredients.append([])
            all_ingredients[1].append(recipe.id)
            all_ingredients[1].append(form.ingredient2.id)
            all_ingredients[1].append(form.ingredient_prep2.data)
            all_ingredients[1].append(form.amount2.data)
            all_ingredients[1].append(form.unit2.data)
        else:
            ing = Ingredients(form.ingredient_alt2.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[1].append(recipe.id)
            all_ingredients[1].append(ing.id)
            all_ingredients[1].append(form.ingredient_prep2.data)
            all_ingredients[1].append(form.amount2.data)
            all_ingredients[1].append(form.unit2.data)
        
        if form.ingredient_alt3.data == "":
            all_ingredients.append([])
            all_ingredients[2].append(recipe.id)
            all_ingredients[2].append(form.ingredient3.id)
            all_ingredients[2].append(form.ingredient_prep3.data)
            all_ingredients[2].append(form.amount3.data)
            all_ingredients[2].append(form.unit3.data)
        else:
            ing = Ingredients(form.ingredient_alt3.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[2].append(recipe.id)
            all_ingredients[2].append(ing.id)
            all_ingredients[2].append(form.ingredient_prep1.data)
            all_ingredients[2].append(form.amount3.data)
            all_ingredients[2].append(form.unit3.data)
        
        if form.ingredient_alt4.data == "":
            all_ingredients.append([])
            all_ingredients[3].append(recipe.id)
            all_ingredients[3].append(form.ingredient4.id)
            all_ingredients[3].append(form.ingredient_prep4.data)
            all_ingredients[3].append(form.amount4.data)
            all_ingredients[3].append(form.unit4.data)
        else:
            ing = Ingredients(form.ingredient_alt4.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[3].append(recipe.id)
            all_ingredients[3].append(ing.id)
            all_ingredients[3].append(form.ingredient_prep4.data)
            all_ingredients[3].append(form.amount4.data)
            all_ingredients[3].append(form.unit4.data)
        
        if form.ingredient_alt5.data == "":
            all_ingredients.append([])
            all_ingredients[4].append(recipe.id)
            all_ingredients[4].append(form.ingredient5.id)
            all_ingredients[4].append(form.ingredient_prep5.data)
            all_ingredients[4].append(form.amount5.data)
            all_ingredients[4].append(form.unit5.data)
        else:
            ing = Ingredients(form.ingredient_alt5.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[4].append(recipe.id)
            all_ingredients[4].append(ing.id)
            all_ingredients[4].append(form.ingredient_prep5.data)
            all_ingredients[4].append(form.amount5.data)
            all_ingredients[4].append(form.unit5.data)
        
        if form.ingredient_alt6.data == "":
            all_ingredients.append([])
            all_ingredients[5].append(recipe.id)
            all_ingredients[5].append(form.ingredient6.id)
            all_ingredients[5].append(form.ingredient_prep6.data)
            all_ingredients[5].append(form.amount6.data)
            all_ingredients[5].append(form.unit6.data)
        else:
            ing = Ingredients(form.ingredient_alt6.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[5].append(recipe.id)
            all_ingredients[5].append(ing.id)
            all_ingredients[5].append(form.ingredient_prep6.data)
            all_ingredients[5].append(form.amount6.data)
            all_ingredients[5].append(form.unit6.data)
        
        if form.ingredient_alt7.data == "":
            all_ingredients.append([])
            all_ingredients[6].append(recipe.id)
            all_ingredients[6].append(form.ingredient7.id)
            all_ingredients[6].append(form.ingredient_prep7.data)
            all_ingredients[6].append(form.amount7.data)
            all_ingredients[6].append(form.unit7.data)
        else:
            ing = Ingredients(form.ingredient_alt7.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[6].append(recipe.id)
            all_ingredients[6].append(ing.id)
            all_ingredients[6].append(form.ingredient_prep7.data)
            all_ingredients[6].append(form.amount7.data)
            all_ingredients[6].append(form.unit7.data)
        
        if form.ingredient_alt8.data == "":
            all_ingredients.append([])
            all_ingredients[7].append(recipe.id)
            all_ingredients[7].append(form.ingredient8.id)
            all_ingredients[7].append(form.ingredient_prep8.data)
            all_ingredients[7].append(form.amount8.data)
            all_ingredients[7].append(form.unit8.data)
        else:
            ing = Ingredients(form.ingredient_alt8.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[7].append(recipe.id)
            all_ingredients[7].append(ing.id)
            all_ingredients[7].append(form.ingredient_prep8.data)
            all_ingredients[7].append(form.amount8.data)
            all_ingredients[7].append(form.unit8.data)
        
        if form.ingredient_alt9.data == "":
            all_ingredients.append([])
            all_ingredients[8].append(recipe.id)
            all_ingredients[8].append(form.ingredient9.id)
            all_ingredients[8].append(form.ingredient_prep9.data)
            all_ingredients[8].append(form.amount9.data)
            all_ingredients[8].append(form.unit9.data)
        else:
            ing = Ingredients(form.ingredient_alt9.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[8].append(recipe.id)
            all_ingredients[8].append(ing.id)
            all_ingredients[8].append(form.ingredient_prep9.data)
            all_ingredients[8].append(form.amount9.data)
            all_ingredients[8].append(form.unit9.data)
        
        if form.ingredient_alt10.data == "":
            all_ingredients.append([])
            all_ingredients[9].append(recipe.id)
            all_ingredients[9].append(form.ingredient10.id)
            all_ingredients[9].append(form.ingredient_prep1.data)
            all_ingredients[9].append(form.amount10.data)
            all_ingredients[9].append(form.unit10.data)
        else:
            ing = Ingredients(form.ingredient_alt10.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[9].append(recipe.id)
            all_ingredients[9].append(ing.id)
            all_ingredients[9].append(form.ingredient_prep10.data)
            all_ingredients[9].append(form.amount10.data)
            all_ingredients[9].append(form.unit10.data)

        if form.ingredient_alt11.data == "":
            all_ingredients.append([])
            all_ingredients[10].append(recipe.id)
            all_ingredients[10].append(form.ingredient11.id)
            all_ingredients[10].append(form.ingredient_prep1.data)
            all_ingredients[10].append(form.amount11.data)
            all_ingredients[10].append(form.unit11.data)
        else:
            ing = Ingredients(form.ingredient_alt1.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[10].append(recipe.id)
            all_ingredients[10].append(ing.id)
            all_ingredients[10].append(form.ingredient_prep11.data)
            all_ingredients[10].append(form.amount11.data)
            all_ingredients[10].append(form.unit11.data)

        if form.ingredient_alt12.data == "":
            all_ingredients.append([])
            all_ingredients[11].append(recipe.id)
            all_ingredients[11].append(form.ingredient12.id)
            all_ingredients[11].append(form.ingredient_prep12.data)
            all_ingredients[11].append(form.amount12.data)
            all_ingredients[11].append(form.unit12.data)
        else:
            ing = Ingredients(form.ingredient_alt12.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[11].append(recipe.id)
            all_ingredients[11].append(ing.id)
            all_ingredients[11].append(form.ingredient_prep12.data)
            all_ingredients[11].append(form.amount12.data)
            all_ingredients[11].append(form.unit12.data)

        if form.ingredient_alt13.data == "":
            all_ingredients.append([])
            all_ingredients[12].append(recipe.id)
            all_ingredients[12].append(form.ingredient13.id)
            all_ingredients[12].append(form.ingredient_prep13.data)
            all_ingredients[12].append(form.amount13.data)
            all_ingredients[12].append(form.unit13.data)
        else:
            ing = Ingredients(form.ingredient_alt13.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[12].append(recipe.id)
            all_ingredients[12].append(ing.id)
            all_ingredients[12].append(form.ingredient_prep13.data)
            all_ingredients[12].append(form.amount13.data)
            all_ingredients[12].append(form.unit13.data)

        if form.ingredient_alt14.data == "":
            all_ingredients.append([])
            all_ingredients[13].append(recipe.id)
            all_ingredients[13].append(form.ingredient14.id)
            all_ingredients[13].append(form.ingredient_prep14.data)
            all_ingredients[13].append(form.amount14.data)
            all_ingredients[13].append(form.unit14.data)
        else:
            ing = Ingredients(form.ingredient_alt14.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[13].append(recipe.id)
            all_ingredients[13].append(ing.id)
            all_ingredients[13].append(form.ingredient_prep14.data)
            all_ingredients[13].append(form.amount14.data)
            all_ingredients[13].append(form.unit14.data)

        if form.ingredient_alt15.data == "":
            all_ingredients.append([])
            all_ingredients[14].append(recipe.id)
            all_ingredients[14].append(form.ingredient15.id)
            all_ingredients[14].append(form.ingredient_prep15.data)
            all_ingredients[14].append(form.amount15.data)
            all_ingredients[14].append(form.unit15.data)
        else:
            ing = Ingredients(form.ingredient_alt15.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[14].append(recipe.id)
            all_ingredients[14].append(ing.id)
            all_ingredients[14].append(form.ingredient_prep15.data)
            all_ingredients[14].append(form.amount15.data)
            all_ingredients[14].append(form.unit15.data)

        if form.ingredient_alt16.data == "":
            all_ingredients.append([])
            all_ingredients[15].append(recipe.id)
            all_ingredients[15].append(form.ingredient16.id)
            all_ingredients[15].append(form.ingredient_prep16.data)
            all_ingredients[15].append(form.amount16.data)
            all_ingredients[15].append(form.unit16.data)
        else:
            ing = Ingredients(form.ingredient_alt16.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[15].append(recipe.id)
            all_ingredients[15].append(ing.id)
            all_ingredients[15].append(form.ingredient_prep16.data)
            all_ingredients[15].append(form.amount16.data)
            all_ingredients[15].append(form.unit16.data)

        if form.ingredient_alt17.data == "":
            all_ingredients.append([])
            all_ingredients[16].append(recipe.id)
            all_ingredients[16].append(form.ingredient17.id)
            all_ingredients[16].append(form.ingredient_prep17.data)
            all_ingredients[16].append(form.amount17.data)
            all_ingredients[16].append(form.unit17.data)
        else:
            ing = Ingredients(form.ingredient_alt17.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[16].append(recipe.id)
            all_ingredients[16].append(ing.id)
            all_ingredients[16].append(form.ingredient_prep17.data)
            all_ingredients[16].append(form.amount17.data)
            all_ingredients[16].append(form.unit17.data)

        if form.ingredient_alt18.data == "":
            all_ingredients.append([])
            all_ingredients[17].append(recipe.id)
            all_ingredients[17].append(form.ingredient18.id)
            all_ingredients[17].append(form.ingredient_prep18.data)
            all_ingredients[17].append(form.amount18.data)
            all_ingredients[17].append(form.unit18.data)
        else:
            ing = Ingredients(form.ingredient_alt18.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[17].append(recipe.id)
            all_ingredients[17].append(ing.id)
            all_ingredients[17].append(form.ingredient_prep18.data)
            all_ingredients[17].append(form.amount18.data)
            all_ingredients[17].append(form.unit18.data)

        if form.ingredient_alt19.data == "":
            all_ingredients.append([])
            all_ingredients[18].append(recipe.id)
            all_ingredients[18].append(form.ingredient19.id)
            all_ingredients[18].append(form.ingredient_prep19.data)
            all_ingredients[18].append(form.amount19.data)
            all_ingredients[18].append(form.unit19.data)
        else:
            ing = Ingredients(form.ingredient_alt19.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[18].append(recipe.id)
            all_ingredients[18].append(ing.id)
            all_ingredients[18].append(form.ingredient_prep19.data)
            all_ingredients[18].append(form.amount19.data)
            all_ingredients[18].append(form.unit19.data)

        if form.ingredient_alt20.data == "":
            all_ingredients.append([])
            all_ingredients[19].append(recipe.id)
            all_ingredients[19].append(form.ingredient20.id)
            all_ingredients[19].append(form.ingredient_prep20.data)
            all_ingredients[19].append(form.amount20.data)
            all_ingredients[19].append(form.unit20.data)
        else:
            ing = Ingredients(form.ingredient_alt20.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[19].append(recipe.id)
            all_ingredients[19].append(ing.id)
            all_ingredients[19].append(form.ingredient_prep20.data)
            all_ingredients[19].append(form.amount20.data)
            all_ingredients[19].append(form.unit20.data)

        if form.ingredient_alt21.data == "":
            all_ingredients.append([])
            all_ingredients[20].append(recipe.id)
            all_ingredients[20].append(form.ingredient21.id)
            all_ingredients[20].append(form.ingredient_prep21.data)
            all_ingredients[20].append(form.amount21.data)
            all_ingredients[20].append(form.unit21.data)
        else:
            ing = Ingredients(form.ingredient_alt21.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[20].append(recipe.id)
            all_ingredients[20].append(ing.id)
            all_ingredients[20].append(form.ingredient_prep21.data)
            all_ingredients[20].append(form.amount21.data)
            all_ingredients[20].append(form.unit21.data)

        
        if form.ingredient_alt22.data == "":
            all_ingredients.append([])
            all_ingredients[21].append(recipe.id)
            all_ingredients[21].append(form.ingredient22.id)
            all_ingredients[21].append(form.ingredient_prep22.data)
            all_ingredients[21].append(form.amount22.data)
            all_ingredients[21].append(form.unit22.data)
        else:
            ing = Ingredients(form.ingredient_alt22.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[21].append(recipe.id)
            all_ingredients[21].append(ing.id)
            all_ingredients[21].append(form.ingredient_prep22.data)
            all_ingredients[21].append(form.amount22.data)
            all_ingredients[21].append(form.unit22.data)

        if form.ingredient_alt23.data == "":
            all_ingredients.append([])
            all_ingredients[22].append(recipe.id)
            all_ingredients[22].append(form.ingredient23.id)
            all_ingredients[22].append(form.ingredient_prep23.data)
            all_ingredients[22].append(form.amount23.data)
            all_ingredients[22].append(form.unit23.data)
        else:
            ing = Ingredients(form.ingredient_alt23.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[22].append(recipe.id)
            all_ingredients[22].append(ing.id)
            all_ingredients[22].append(form.ingredient_prep23.data)
            all_ingredients[22].append(form.amount23.data)
            all_ingredients[22].append(form.unit23.data)

        if form.ingredient_alt24.data == "":
            all_ingredients.append([])
            all_ingredients[23].append(recipe.id)
            all_ingredients[23].append(form.ingredient24.id)
            all_ingredients[23].append(form.ingredient_prep24.data)
            all_ingredients[23].append(form.amount24.data)
            all_ingredients[23].append(form.unit24.data)
        else:
            ing = Ingredients(form.ingredient_alt24.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[23].append(recipe.id)
            all_ingredients[23].append(ing.id)
            all_ingredients[23].append(form.ingredient_prep24.data)
            all_ingredients[23].append(form.amount24.data)
            all_ingredients[23].append(form.unit24.data)

        if form.ingredient_alt25.data == "":
            all_ingredients.append([])
            all_ingredients[24].append(recipe.id)
            all_ingredients[24].append(form.ingredient25.id)
            all_ingredients[24].append(form.ingredient_prep25.data)
            all_ingredients[24].append(form.amount25.data)
            all_ingredients[24].append(form.unit25.data)
        else:
            ing = Ingredients(form.ingredient_alt25.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[24].append(recipe.id)
            all_ingredients[24].append(ing.id)
            all_ingredients[24].append(form.ingredient_prep25.data)
            all_ingredients[24].append(form.amount25.data)
            all_ingredients[24].append(form.unit25.data)

        if form.ingredient_alt26.data == "":
            all_ingredients.append([])
            all_ingredients[25].append(recipe.id)
            all_ingredients[25].append(form.ingredient26.id)
            all_ingredients[25].append(form.ingredient_prep26.data)
            all_ingredients[25].append(form.amount26.data)
            all_ingredients[25].append(form.unit26.data)
        else:
            ing = Ingredients(form.ingredient_alt26.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[25].append(recipe.id)
            all_ingredients[25].append(ing.id)
            all_ingredients[25].append(form.ingredient_prep26.data)
            all_ingredients[25].append(form.amount26.data)
            all_ingredients[25].append(form.unit26.data)

        if form.ingredient_alt27.data == "":
            all_ingredients.append([])
            all_ingredients[26].append(recipe.id)
            all_ingredients[26].append(form.ingredient27.id)
            all_ingredients[26].append(form.ingredient_prep27.data)
            all_ingredients[26].append(form.amount27.data)
            all_ingredients[26].append(form.unit27.data)
        else:
            ing = Ingredients(form.ingredient_alt27.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[26].append(recipe.id)
            all_ingredients[26].append(ing.id)
            all_ingredients[26].append(form.ingredient_prep27.data)
            all_ingredients[26].append(form.amount27.data)
            all_ingredients[26].append(form.unit27.data)

        if form.ingredient_alt28.data == "":
            all_ingredients.append([])
            all_ingredients[27].append(recipe.id)
            all_ingredients[27].append(form.ingredient28.id)
            all_ingredients[27].append(form.ingredient_prep28.data)
            all_ingredients[27].append(form.amount28.data)
            all_ingredients[27].append(form.unit28.data)
        else:
            ing = Ingredients(form.ingredient_alt28.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[27].append(recipe.id)
            all_ingredients[27].append(ing.id)
            all_ingredients[27].append(form.ingredient_prep28.data)
            all_ingredients[27].append(form.amount28.data)
            all_ingredients[27].append(form.unit28.data)

        if form.ingredient_alt29.data == "":
            all_ingredients.append([])
            all_ingredients[28].append(recipe.id)
            all_ingredients[28].append(form.ingredient29.id)
            all_ingredients[28].append(form.ingredient_prep29.data)
            all_ingredients[28].append(form.amount29.data)
            all_ingredients[28].append(form.unit29.data)
        else:
            ing = Ingredients(form.ingredient_alt29.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[28].append(recipe.id)
            all_ingredients[28].append(ing.id)
            all_ingredients[28].append(form.ingredient_prep29.data)
            all_ingredients[28].append(form.amount29.data)
            all_ingredients[28].append(form.unit29.data)

        if form.ingredient_alt30.data == "":
            all_ingredients.append([])
            all_ingredients[29].append(recipe.id)
            all_ingredients[29].append(form.ingredient30.id)
            all_ingredients[29].append(form.ingredient_prep30.data)
            all_ingredients[29].append(form.amount30.data)
            all_ingredients[29].append(form.unit30.data)
        else:
            ing = Ingredients(form.ingredient_alt30.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients.append([])
            all_ingredients[29].append(recipe.id)
            all_ingredients[29].append(ing.id)
            all_ingredients[29].append(form.ingredient_prep30.data)
            all_ingredients[29].append(form.amount30.data)
            all_ingredients[29].append(form.unit30.data)

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
    
        return render_template('add_recipe.html', recipe = recipe)
    else:
        return render_template('add_recipe.html', form=form)