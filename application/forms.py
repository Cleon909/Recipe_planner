from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField, FormField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
# from application.models import Ingredients, Cuisine, Recipes, Quantity, Method


class AddRecipeForm(FlaskForm):
    name = StringField('Name of Recipe', validators = [DataRequired(), Length(max = 200)])
    recipe_description = StringField('Details of recipe(i.e. cooking time, calories, macros etc', validators = [(Length(max = 500))])
    cuisine = SelectField('Type of Cuisine', choices = [])
    

    all_ingredients = []

    submit = SubmitField('Press to add recipe')
    no_of_ingredients = SelectField('Number of Ingredients',choices = [i for i in range(1, 31)])
    ingredient1 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt1 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient2 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt2 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient3 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt3 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient4 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt4 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient5 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt5 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient6 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt6 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient7 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt7 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient8 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt8 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient9 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt9 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient10 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt10 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient11 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt11 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient12 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt12 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient13 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt13 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient14 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt14 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient15 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt15 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient16 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt16 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient17 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt17 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient18 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt18 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient19 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt19 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient20 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt20 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient21 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt21 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient22 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt22 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient23 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt23 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient24 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt24 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient25 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt25 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient26 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt26 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient27 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt27 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient28 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt28 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient29 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt29 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    ingredient30 = SelectField('Choose Ingredients', choices = [])
    ingredient_alt30 = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    
   
    amount1 = DecimalField('Amount')
    unit1 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount2 = DecimalField('Amount')
    unit2 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount3 = DecimalField('Amount')
    unit3 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount4 = DecimalField('Amount')
    unit4 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount5 = DecimalField('Amount')
    unit5 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount6 = DecimalField('Amount')
    unit6 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount7 = DecimalField('Amount')
    unit7 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount8 = DecimalField('Amount')
    unit8 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount9 = DecimalField('Amount')
    unit9 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount10 = DecimalField('Amount')
    unit10 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount11 = DecimalField('Amount')
    unit11 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount12 = DecimalField('Amount')
    unit12 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount13 = DecimalField('Amount')
    unit13 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount14 = DecimalField('Amount')
    unit14 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount15 = DecimalField('Amount')
    unit15 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount16 = DecimalField('Amount')
    unit16 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount17 = DecimalField('Amount')
    unit17 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount18 = DecimalField('Amount')
    unit18 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount19 = DecimalField('Amount')
    unit19 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount20 = DecimalField('Amount')
    unit20 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount21 = DecimalField('Amount')
    unit21 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount22 = DecimalField('Amount')
    unit22 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount23 = DecimalField('Amount')
    unit23 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount24 = DecimalField('Amount')
    unit24 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount25 = DecimalField('Amount')
    unit25 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount26 = DecimalField('Amount')
    unit26 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount27 = DecimalField('Amount')
    unit27 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount28 = DecimalField('Amount')
    unit28 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount29 = DecimalField('Amount')
    unit29 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    amount30 = DecimalField('Amount')
    unit30 = StringField('Unit of Measurement', validators = [(Length(max = 10))])

    
    ingredient_prep1 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators = [Length(max=100)])
    ingredient_prep2 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators = [Length(max=100)])
    ingredient_prep3 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators = [Length(max=100)])
    ingredient_prep4 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep5 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep6 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep7 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep8 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep9 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep10 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep11 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep12 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep13 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep14 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep15 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep16 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep17 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep18 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep19 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep20 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep21 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep22 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep23 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep24 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep25 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep26 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep27 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep28 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep29 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    ingredient_prep30 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])


    # no_of_ingredients = SelectField('Number of Ingredients',choices = [i for i in range(1, 31)])
    # ingredient1 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt1 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient2 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt2 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient3 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt3 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient4 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt4 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient5 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt5 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient6 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt6 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient7 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt7 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient8 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt8 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient9 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt9 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient10 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt10 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient11 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt11 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient12 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt12 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient13 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt13 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient14 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt14 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient15 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt15 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient16 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt16 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient17 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt17 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient18 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt18 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient19 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt19 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient20 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt20 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient21 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt21 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient22 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt22 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient23 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt23 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient24 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt24 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient25 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt25 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient26 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt26 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient27 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt27 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient28 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt28 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient29 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt29 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    # ingredient30 = SelectField('Choose Ingredients', choices = [])
    # ingredient_alt30 = StringField('If ingredient not in list type here', validators = [Length(max = 50)])
    
   
    # amount1 = DecimalField('Amount')
    # unit1 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount2 = DecimalField('Amount')
    # unit2 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount3 = DecimalField('Amount')
    # unit3 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount4 = DecimalField('Amount')
    # unit4 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount5 = DecimalField('Amount')
    # unit5 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount6 = DecimalField('Amount')
    # unit6 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount7 = DecimalField('Amount')
    # unit7 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount8 = DecimalField('Amount')
    # unit8 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount9 = DecimalField('Amount')
    # unit9 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount10 = DecimalField('Amount')
    # unit10 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount11 = DecimalField('Amount')
    # unit11 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount12 = DecimalField('Amount')
    # unit12 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount13 = DecimalField('Amount')
    # unit13 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount14 = DecimalField('Amount')
    # unit14 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount15 = DecimalField('Amount')
    # unit15 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount16 = DecimalField('Amount')
    # unit16 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount17 = DecimalField('Amount')
    # unit17 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount18 = DecimalField('Amount')
    # unit18 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount19 = DecimalField('Amount')
    # unit19 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount20 = DecimalField('Amount')
    # unit20 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount21 = DecimalField('Amount')
    # unit21 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount22 = DecimalField('Amount')
    # unit22 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount23 = DecimalField('Amount')
    # unit23 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount24 = DecimalField('Amount')
    # unit24 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount25 = DecimalField('Amount')
    # unit25 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount26 = DecimalField('Amount')
    # unit26 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount27 = DecimalField('Amount')
    # unit27 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount28 = DecimalField('Amount')
    # unit28 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount29 = DecimalField('Amount')
    # unit29 = StringField('Unit of Measurement', validators = [(Length(max = 10))])
    # amount30 = DecimalField('Amount')
    # unit30 = StringField('Unit of Measurement', validators = [(Length(max = 10))])

    
    # ingredient_prep1 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep2 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep3 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep4 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep5 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep6 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep7 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep8 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep9 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep10 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep11 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep12 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep13 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep14 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep15 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep16 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep17 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep18 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep19 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep20 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep21 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep22 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep23 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep24 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep25 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep26 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep27 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep28 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep29 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])
    # ingredient_prep30 = StringField('chopped, sliced etc. Leave blank if no prep needed', validators =[Length(max=100)])



    how_many_steps = SelectField('How many steps', choices = [i for i in range(1, 15)])
    method1 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method2 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method3 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method4 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method5 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method6 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method7 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method8 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method9 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method10 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method11 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method12 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method13 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method14 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")
    method15 = StringField('Input method of making the recipe in steps', validators = [Length(max=200)], default = "")

    
    