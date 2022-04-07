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
        
        # quantity = []
        # if form.ingredient_alt1.data == "":
        #     quantity.append[0](recipe.id)
        #     quantity.append[0](form.ingredient1.id)
        #     quantity.append[0](form.ingredient_prep.data)
        #     quantity.append[0](form.amount.data)
        #     quantity.append[0](form.unit.data)
        #     quant = Quantity(quantity[0][0],quantity[0][1],quantity[0][2],quantity[0][3],quantity[0][4])
        #     db.session.add(quant)
        #     db.session.commit()
        # else:
        #     ing = Ingredients(form.ingredient_alt1.data)
        #     db.session.add(ing)
        #     db.session.commit()
        #     quantity.append[0](recipe.id)
        #     quantity.append[0](ing.id)
        #     quantity.append[0](form.ingredient_prep.data)
        #     quantity.append[0](form.amount.data)
        #     quantity.append[0](form.unit.data)
        #     quant = Quantity(quantity[0][0],quantity[0][1],quantity[0][2],quantity[0][3],quantity[0][4])
        #     db.session.add(quant)
        #     db.session.commit()


        
        
        # for i in range(1,form.no_of_ingredients.data +1):
        #     if ingredient{i}  
        #     ingredients[i] =  


        all_ingredients = []

        if form.ingredient_alt1 == "":
            all_ingredients[0][0] = recipe.id
            all_ingredients[0][1] = form.ingredient1.id
            all_ingredients[0][2] = form.ingredient_prep1.data
            all_ingredients[0][3] = form.amount1.data
            all_ingredients[0][4] = form.unit1.data
        else:
            ing = Ingredients(form.ingredient_alt.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[0][0] = recipe.id
            all_ingredients[0][1] = ing.id
            all_ingredients[0][2] = form.ingredient_prep1.data
            all_ingredients[0][3] = form.amount1.data
            all_ingredients[0][4] = form.unit1.data

        if form.ingredient_alt2 == "":
            all_ingredients[1][0] = recipe.id
            all_ingredients[1][1] = form.ingredient2.id
            all_ingredients[1][2] = form.ingredient_prep2.data
            all_ingredients[1][3] = form.amount2.data
            all_ingredients[1][4] = form.unit2.data
        else:
            ing = Ingredients(form.ingredient_alt2.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[1][0] = recipe.id
            all_ingredients[1][1] = ing.id
            all_ingredients[1][2] = form.ingredient_prep2.data
            all_ingredients[1][3] = form.amount2.data
            all_ingredients[1][4] = form.unit2.data
            
        if form.ingredient_alt3 == "":
            all_ingredients[2][0] = recipe.id
            all_ingredients[2][1] = form.ingredient3.id
            all_ingredients[2][2] = form.ingredient_prep3.data
            all_ingredients[2][3] = form.amount3.data
            all_ingredients[2][4] = form.unit3.data
        else:
            ing = Ingredients(form.ingredient_alt3.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[2][0] = recipe.id
            all_ingredients[2][1] = ing.id
            all_ingredients[2][2] = form.ingredient_prep3.data
            all_ingredients[2][3] = form.amount3.data
            all_ingredients[2][4] = form.unit3.data
            
        if form.ingredient_alt4 == "":
            all_ingredients[3][0] = recipe.id
            all_ingredients[3][1] = form.ingredient4.id
            all_ingredients[3][2] = form.ingredient_prep4.data
            all_ingredients[3][3] = form.amount4.data
            all_ingredients[3][4] = form.unit4.data
        else:
            ing = Ingredients(form.ingredient_alt4.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[3][0] = recipe.id
            all_ingredients[3][1] = ing.id
            all_ingredients[3][2] = form.ingredient_prep4.data
            all_ingredients[3][3] = form.amount4.data
            all_ingredients[3][4] = form.unit4.data
            
        if form.ingredient_alt5 == "":
            all_ingredients[4][0] = recipe.id
            all_ingredients[4][1] = form.ingredient5.id
            all_ingredients[4][2] = form.ingredient_prep5.data
            all_ingredients[4][3] = form.amount5.data
            all_ingredients[4][4] = form.unit5.data
        else:
            ing = Ingredients(form.ingredient_alt5.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[4][0] = recipe.id
            all_ingredients[4][1] = ing.id
            all_ingredients[4][2] = form.ingredient_prep5.data
            all_ingredients[4][3] = form.amount5.data
            all_ingredients[4][4] = form.unit5.data
            
        if form.ingredient_alt6 == "":
            all_ingredients[5][0] = recipe.id
            all_ingredients[5][1] = form.ingredient6.id
            all_ingredients[5][2] = form.ingredient_prep6.data
            all_ingredients[5][3] = form.amount6.data
            all_ingredients[5][4] = form.unit6.data
        else:
            ing = Ingredients(form.ingredient_alt6.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[5][0] = recipe.id
            all_ingredients[5][1] = ing.id
            all_ingredients[5][2] = form.ingredient_prep6.data
            all_ingredients[5][3] = form.amount6.data
            all_ingredients[5][4] = form.unit6.data
            
        if form.ingredient_alt7 == "":
            all_ingredients[6][0] = recipe.id
            all_ingredients[6][1] = form.ingredient7.id
            all_ingredients[6][2] = form.ingredient_prep7.data
            all_ingredients[6][3] = form.amount7.data
            all_ingredients[6][4] = form.unit7.data
        else:
            ing = Ingredients(form.ingredient_alt7.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[6][0] = recipe.id
            all_ingredients[6][1] = ing.id
            all_ingredients[6][2] = form.ingredient_prep7.data
            all_ingredients[6][3] = form.amount7.data
            all_ingredients[6][4] = form.unit7.data
            
        if form.ingredient_alt8 == "":
            all_ingredients[7][0] = recipe.id
            all_ingredients[7][1] = form.ingredient8.id
            all_ingredients[7][2] = form.ingredient_prep8.data
            all_ingredients[7][3] = form.amount8.data
            all_ingredients[7][4] = form.unit8.data
        else:
            ing = Ingredients(form.ingredient_alt8.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[7][0] = recipe.id
            all_ingredients[7][1] = ing.id
            all_ingredients[7][2] = form.ingredient_prep8.data
            all_ingredients[7][3] = form.amount8.data
            all_ingredients[7][4] = form.unit8.data
            
        if form.ingredient_alt9 == "":
            all_ingredients[8][0] = recipe.id
            all_ingredients[8][1] = form.ingredient9.id
            all_ingredients[8][2] = form.ingredient_prep9.data
            all_ingredients[8][3] = form.amount9.data
            all_ingredients[8][4] = form.unit9.data
        else:
            ing = Ingredients(form.ingredient_alt9.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[8][0] = recipe.id
            all_ingredients[8][1] = ing.id
            all_ingredients[8][2] = form.ingredient_prep9.data
            all_ingredients[8][3] = form.amount9.data
            all_ingredients[8][4] = form.unit9.data
            
        if form.ingredient_alt10 == "":
            all_ingredients[9][0] = recipe.id
            all_ingredients[9][1] = form.ingredient10.id
            all_ingredients[9][2] = form.ingredient_prep10.data
            all_ingredients[9][3] = form.amount10.data
            all_ingredients[9][4] = form.unit10.data
        else:
            ing = Ingredients(form.ingredient_alt10.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[9][0] = recipe.id
            all_ingredients[9][1] = ing.id
            all_ingredients[9][2] = form.ingredient_prep10.data
            all_ingredients[9][3] = form.amount10.data
            all_ingredients[9][4] = form.unit10.data

        if form.ingredient_alt11 == "":
            all_ingredients[10][0] = recipe.id
            all_ingredients[10][1] = form.ingredient11.id
            all_ingredients[10][2] = form.ingredient_prep11.data
            all_ingredients[10][3] = form.amount11.data
            all_ingredients[10][4] = form.unit11.data
        else:
            ing = Ingredients(form.ingredient_alt1.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[10][0] = recipe.id
            all_ingredients[10][1] = ing.id
            all_ingredients[10][2] = form.ingredient_prep11.data
            all_ingredients[10][3] = form.amount11.data
            all_ingredients[10][4] = form.unit11.data

        if form.ingredient_alt12 == "":
            all_ingredients[11][0] = recipe.id
            all_ingredients[11][1] = form.ingredient12.id
            all_ingredients[11][2] = form.ingredient_prep12.data
            all_ingredients[11][3] = form.amount12.data
            all_ingredients[11][4] = form.unit12.data
        else:
            ing = Ingredients(form.ingredient_alt12.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[11][0] = recipe.id
            all_ingredients[11][1] = ing.id
            all_ingredients[11][2] = form.ingredient_prep12.data
            all_ingredients[11][3] = form.amount12.data
            all_ingredients[11][4] = form.unit12.data

        if form.ingredient_alt13 == "":
            all_ingredients[12][0] = recipe.id
            all_ingredients[12][1] = form.ingredient13.id
            all_ingredients[12][2] = form.ingredient_prep13.data
            all_ingredients[12][3] = form.amount13.data
            all_ingredients[12][4] = form.unit13.data
        else:
            ing = Ingredients(form.ingredient_alt13.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[12][0] = recipe.id
            all_ingredients[12][1] = ing.id
            all_ingredients[12][2] = form.ingredient_prep13.data
            all_ingredients[12][3] = form.amount13.data
            all_ingredients[12][4] = form.unit13.data

        if form.ingredient_alt14 == "":
            all_ingredients[13][0] = recipe.id
            all_ingredients[13][1] = form.ingredient14.id
            all_ingredients[13][2] = form.ingredient_prep14.data
            all_ingredients[13][3] = form.amount14.data
            all_ingredients[13][4] = form.unit14.data
        else:
            ing = Ingredients(form.ingredient_alt14.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[13][0] = recipe.id
            all_ingredients[13][1] = ing.id
            all_ingredients[13][2] = form.ingredient_prep14.data
            all_ingredients[13][3] = form.amount14.data
            all_ingredients[13][4] = form.unit14.data

        if form.ingredient_alt15 == "":
            all_ingredients[14][0] = recipe.id
            all_ingredients[14][1] = form.ingredient15.id
            all_ingredients[14][2] = form.ingredient_prep15.data
            all_ingredients[14][3] = form.amount15.data
            all_ingredients[14][4] = form.unit15.data
        else:
            ing = Ingredients(form.ingredient_alt15.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[14][0] = recipe.id
            all_ingredients[14][1] = ing.id
            all_ingredients[14][2] = form.ingredient_prep15.data
            all_ingredients[14][3] = form.amount15.data
            all_ingredients[14][4] = form.unit15.data

        if form.ingredient_alt16 == "":
            all_ingredients[15][0] = recipe.id
            all_ingredients[15][1] = form.ingredient16.id
            all_ingredients[15][2] = form.ingredient_prep16.data
            all_ingredients[15][3] = form.amount16.data
            all_ingredients[15][4] = form.unit16.data
        else:
            ing = Ingredients(form.ingredient_alt16.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[15][0] = recipe.id
            all_ingredients[15][1] = ing.id
            all_ingredients[15][2] = form.ingredient_prep16.data
            all_ingredients[15][3] = form.amount16.data
            all_ingredients[15][4] = form.unit16.data

        if form.ingredient_alt17 == "":
            all_ingredients[16][0] = recipe.id
            all_ingredients[16][1] = form.ingredient17.id
            all_ingredients[16][2] = form.ingredient_prep17.data
            all_ingredients[16][3] = form.amount17.data
            all_ingredients[16][4] = form.unit17.data
        else:
            ing = Ingredients(form.ingredient_alt17.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[16][0] = recipe.id
            all_ingredients[16][1] = ing.id
            all_ingredients[16][2] = form.ingredient_prep17.data
            all_ingredients[16][3] = form.amount17.data
            all_ingredients[16][4] = form.unit17.data

        if form.ingredient_alt18 == "":
            all_ingredients[17][0] = recipe.id
            all_ingredients[17][1] = form.ingredient18.id
            all_ingredients[17][2] = form.ingredient_prep18.data
            all_ingredients[17][3] = form.amount18.data
            all_ingredients[17][4] = form.unit18.data
        else:
            ing = Ingredients(form.ingredient_alt18.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[17][0] = recipe.id
            all_ingredients[17][1] = ing.id
            all_ingredients[17][2] = form.ingredient_prep18.data
            all_ingredients[17][3] = form.amount18.data
            all_ingredients[17][4] = form.unit18.data

        if form.ingredient_alt19 == "":
            all_ingredients[18][0] = recipe.id
            all_ingredients[18][1] = form.ingredient19.id
            all_ingredients[18][2] = form.ingredient_prep19.data
            all_ingredients[18][3] = form.amount19.data
            all_ingredients[18][4] = form.unit19.data
        else:
            ing = Ingredients(form.ingredient_alt19.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[18][0] = recipe.id
            all_ingredients[18][1] = ing.id
            all_ingredients[18][2] = form.ingredient_prep19.data
            all_ingredients[18][3] = form.amount19.data
            all_ingredients[18][4] = form.unit19.data

        if form.ingredient_alt20 == "":
            all_ingredients[19][0] = recipe.id
            all_ingredients[19][1] = form.ingredient20.id
            all_ingredients[19][2] = form.ingredient_prep20.data
            all_ingredients[19][3] = form.amount20.data
            all_ingredients[19][4] = form.unit20.data
        else:
            ing = Ingredients(form.ingredient_alt20.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[19][0] = recipe.id
            all_ingredients[19][1] = ing.id
            all_ingredients[19][2] = form.ingredient_prep20.data
            all_ingredients[19][3] = form.amount20.data
            all_ingredients[19][4] = form.unit20.data

        if form.ingredient_alt21 == "":
            all_ingredients[20][0] = recipe.id
            all_ingredients[20][1] = form.ingredient21.id
            all_ingredients[20][2] = form.ingredient_prep21.data
            all_ingredients[20][3] = form.amount21.data
            all_ingredients[20][4] = form.unit21.data
        else:
            ing = Ingredients(form.ingredient_alt21.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[20][0] = recipe.id
            all_ingredients[20][1] = ing.id
            all_ingredients[20][2] = form.ingredient_prep21.data
            all_ingredients[20][3] = form.amount21.data
            all_ingredients[20][4] = form.unit21.data

        if form.ingredient_alt22 == "":
            all_ingredients[21][0] = recipe.id
            all_ingredients[21][1] = form.ingredient22.id
            all_ingredients[21][2] = form.ingredient_prep22.data
            all_ingredients[21][3] = form.amount22.data
            all_ingredients[21][4] = form.unit22.data
        else:
            ing = Ingredients(form.ingredient_alt22.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[21][0] = recipe.id
            all_ingredients[21][1] = ing.id
            all_ingredients[21][2] = form.ingredient_prep22.data
            all_ingredients[21][3] = form.amount22.data
            all_ingredients[21][4] = form.unit2.data

        if form.ingredient_alt23 == "":
            all_ingredients[22][0] = recipe.id
            all_ingredients[22][1] = form.ingredient23.id
            all_ingredients[22][2] = form.ingredient_prep23.data
            all_ingredients[22][3] = form.amount23.data
            all_ingredients[22][4] = form.unit23.data
        else:
            ing = Ingredients(form.ingredient_alt3.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[22][0] = recipe.id
            all_ingredients[22][1] = ing.id
            all_ingredients[22][2] = form.ingredient_prep23.data
            all_ingredients[22][3] = form.amount23.data
            all_ingredients[22][4] = form.unit23.data

        if form.ingredient_alt24 == "":
            all_ingredients[23][0] = recipe.id
            all_ingredients[23][1] = form.ingredient24.id
            all_ingredients[23][2] = form.ingredient_prep24.data
            all_ingredients[23][3] = form.amount24.data
            all_ingredients[23][4] = form.unit24.data
        else:
            ing = Ingredients(form.ingredient_alt24.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[23][0] = recipe.id
            all_ingredients[23][1] = ing.id
            all_ingredients[23][2] = form.ingredient_prep24.data
            all_ingredients[23][3] = form.amount24.data
            all_ingredients[23][4] = form.unit24.data

        if form.ingredient_alt25 == "":
            all_ingredients[24][0] = recipe.id
            all_ingredients[24][1] = form.ingredient25.id
            all_ingredients[24][2] = form.ingredient_prep25.data
            all_ingredients[24][3] = form.amount25.data
            all_ingredients[24][4] = form.unit25.data
        else:
            ing = Ingredients(form.ingredient_alt25.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[24][0] = recipe.id
            all_ingredients[24][1] = ing.id
            all_ingredients[24][2] = form.ingredient_prep25.data
            all_ingredients[24][3] = form.amount25.data
            all_ingredients[24][4] = form.unit25.data

        if form.ingredient_alt26 == "":
            all_ingredients[25][0] = recipe.id
            all_ingredients[25][1] = form.ingredient26.id
            all_ingredients[25][2] = form.ingredient_prep26.data
            all_ingredients[25][3] = form.amount26.data
            all_ingredients[25][4] = form.unit26.data
        else:
            ing = Ingredients(form.ingredient_alt26.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[25][0] = recipe.id
            all_ingredients[25][1] = ing.id
            all_ingredients[25][2] = form.ingredient_prep26.data
            all_ingredients[25][3] = form.amount26.data
            all_ingredients[25][4] = form.unit26.data
            
        if form.ingredient_alt27 == "":
            all_ingredients[26][0] = recipe.id
            all_ingredients[26][1] = form.ingredient27.id
            all_ingredients[26][2] = form.ingredient_prep27.data
            all_ingredients[26][3] = form.amount27.data
            all_ingredients[26][4] = form.unit27.data
        else:
            ing = Ingredients(form.ingredient_alt27.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[26][0] = recipe.id
            all_ingredients[26][1] = ing.id
            all_ingredients[26][2] = form.ingredient_prep27.data
            all_ingredients[26][3] = form.amount27.data
            all_ingredients[26][4] = form.unit27.data

        if form.ingredient_alt28 == "":
            all_ingredients[27][0] = recipe.id
            all_ingredients[27][1] = form.ingredient28.id
            all_ingredients[27][2] = form.ingredient_prep28.data
            all_ingredients[27][3] = form.amount28.data
            all_ingredients[27][4] = form.unit28.data
        else:
            ing = Ingredients(form.ingredient_alt28.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[27][0] = recipe.id
            all_ingredients[27][1] = ing.id
            all_ingredients[27][2] = form.ingredient_prep28.data
            all_ingredients[27][3] = form.amount28.data
            all_ingredients[27][4] = form.unit28.data
        
        if form.ingredient_alt29 == "":
            all_ingredients[28][0] = recipe.id
            all_ingredients[28][1] = form.ingredient29.id
            all_ingredients[28][2] = form.ingredient_prep29.data
            all_ingredients[28][3] = form.amount29.data
            all_ingredients[28][4] = form.unit29.data
        else:
            ing = Ingredients(form.ingredient_alt29.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[28][0] = recipe.id
            all_ingredients[28][1] = ing.id
            all_ingredients[28][2] = form.ingredient_prep29.data
            all_ingredients[28][3] = form.amount29.data
            all_ingredients[28][4] = form.unit29.data
        
        if form.ingredient_alt30 == "":
            all_ingredients[29][0] = recipe.id
            all_ingredients[29][1] = form.ingredient30.id
            all_ingredients[29][2] = form.ingredient_prep30.data
            all_ingredients[29][3] = form.amount30.data
            all_ingredients[29][4] = form.unit30.data
        else:
            ing = Ingredients(form.ingredient_alt30.data)
            db.session.add(ing)
            db.session.commit()
            all_ingredients[29][0] = recipe.id
            all_ingredients[29][1] = ing.id
            all_ingredients[29][2] = form.ingredient_prep30.data
            all_ingredients[29][3] = form.amount30.data
            all_ingredients[29][4] = form.unit30.data
        

        for i in all_ingredients:
            if i[0] != 0:
                quant = Quantity(all_ingredients[0], all_ingredients[1], all_ingredients[2], all_ingredients[3], all_ingredients[4])
                db.session.add(quant)
                db.commit()
            else:
                continue

        for s in form.method:
            if s.data == NULL:
                continue
            else:
                step = Method(s.data)
                db.session.add(step)
                db.commit()
    
        return render_template('add_recipe.html', recipe = recipe)
    else:
        return render_template('add_recipe.html', form=form)