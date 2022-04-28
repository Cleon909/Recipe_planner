from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField, FormField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import ShoppingList


class AddMetaForm(FlaskForm):
    cuisine = StringField('Enter Cuisine to add', validators = [Length(max = 50 )])
    ingredient = StringField('Enter Ingredient to add', validators = [Length(max = 50)])
    measure = StringField('Enter a measurement unit to add', validators = [Length(max = 10)])
    submit = SubmitField('Press to add')
class SearchForm(FlaskForm):
    recipe = SelectField('pick recipe to show', choices = [])
    submit = SubmitField('Press to show recipe')

class SelectScheduleForm(FlaskForm):
    first_cuisine = SelectField('Cuisine to be included', choices = [])
    second_cuisine = SelectField('Cuisine to be included',choices = [])
    third_cuisine = SelectField('Cuisine to be included', choices = [])
    fourth_cuisine = SelectField('Cuisine to be included', choices = [])
    fifth_cuisine = SelectField('Cuisine to be included', choices = [])
    submit_cuisine = SubmitField('Generate Recipe Schedule')
    
class FinaliseScheduleForm(FlaskForm):
    monday_cb = BooleanField('Change Recipe?')
    tuesday_cb = BooleanField('Change Recipe?')
    wednesday_cb = BooleanField('Change Recipe?')
    thursday_cb = BooleanField('Change Recipe?')
    friday_cb = BooleanField('Change Recipe?')

    monday_recipe = SelectField('Pick a Recipe if you don\'t want the auto generated one', choices = [])
    tuesday_recipe = SelectField('Pick a Recipe if you don\'t want the auto generated one', choices = [])
    wednesday_recipe = SelectField('Pick a Recipe if you don\'t want the auto generated one', choices = [])
    thursday_recipe = SelectField('Pick a Recipe if you don\'t want the auto generated one', choices = [])
    friday_recipe = SelectField('Pick a Recipe if you don\'t want the auto generated one', choices = [])
    submit_recipes = SubmitField('Add recipes to schedule')

class AmendShoppingListForm(FlaskForm):
    shopping_list = ShoppingList.query.all()
    ingredient_id = SelectField(choices = [])
    amount = DecimalField()
    remove = BooleanField("remove ingredient from shopping list?", default = False)
    submit = SubmitField("predd to add updated ingredients to basket")
    form_fields={}
    for ingredient in shopping_list:
        field_id = 'shared_{}'.format(ingredient.amount)
        form_fields[field_id] = DecimalField("Amount", default = ingredient.amount)
    

class AddRecipeForm(FlaskForm):
    name = StringField('Name of Recipe', validators = [DataRequired(), Length(max = 200)])
    recipe_description = TextAreaField('Details of recipe(i.e. cooking time, calories, macros etc', render_kw={'rows':4}, validators = [(Length(max = 500))])
    cuisine = SelectField('Type of Cuisine', choices = [])
    submit = SubmitField('Press to add recipe')
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
    measure1 = SelectField('Unit', choices = [])
    amount2 = DecimalField('Amount')
    measure2 = SelectField('Unit of Measurement', choices = [])
    amount3 = DecimalField('Amount')
    measure3 = SelectField('Unit of Measurement', choices = [])
    amount4 = DecimalField('Amount')
    measure4 = SelectField('Unit of Measurement', choices = [])
    amount5 = DecimalField('Amount')
    measure5 = SelectField('Unit of Measurement', choices = [])
    amount6 = DecimalField('Amount')
    measure6 = SelectField('Unit of Measurement', choices = [])
    amount7 = DecimalField('Amount')
    measure7 = SelectField('Unit of Measurement', choices = [])
    amount8 = DecimalField('Amount')
    measure8 = SelectField('Unit of Measurement', choices = [])
    amount9 = DecimalField('Amount')
    measure9 = SelectField('Unit of Measurement', choices = [])
    amount10 = DecimalField('Amount')
    measure10 = SelectField('Unit of Measurement', choices = [])
    amount11 = DecimalField('Amount')
    measure11 = SelectField('Unit of Measurement', choices = [])
    amount12 = DecimalField('Amount')
    measure12 = SelectField('Unit of Measurement', choices = [])
    amount13 = DecimalField('Amount')
    measure13 = SelectField('Unit of Measurement', choices = [])
    amount14 = DecimalField('Amount')
    measure14 = SelectField('Unit of Measurement', choices = [])
    amount15 = DecimalField('Amount')
    measure15 = SelectField('Unit of Measurement', choices = [])
    amount16 = DecimalField('Amount')
    measure16 = SelectField('Unit of Measurement', choices = [])
    amount17 = DecimalField('Amount')
    measure17 = SelectField('Unit of Measurement', choices = [])
    amount18 = DecimalField('Amount')
    measure18 = SelectField('Unit of Measurement', choices = [])
    amount19 = DecimalField('Amount')
    measure19 = SelectField('Unit of Measurement', choices = [])
    amount20 = DecimalField('Amount')
    measure20 = SelectField('Unit of Measurement', choices = [])
    amount21 = DecimalField('Amount')
    measure21 = SelectField('Unit of Measurement', choices = [])
    amount22 = DecimalField('Amount')
    measure22 = SelectField('Unit of Measurement', choices = [])
    amount23 = DecimalField('Amount')
    measure23 = SelectField('Unit of Measurement', choices = [])
    amount24 = DecimalField('Amount')
    measure24 = SelectField('Unit of Measurement', choices = [])
    amount25 = DecimalField('Amount')
    measure25 = SelectField('Unit of Measurement', choices = [])
    amount26 = DecimalField('Amount')
    measure26 = SelectField('Unit of Measurement', choices = [])
    amount27 = DecimalField('Amount')
    measure27 = SelectField('Unit of Measurement', choices = [])
    amount28 = DecimalField('Amount')
    measure28 = SelectField('Unit of Measurement', choices = [])
    amount29 = DecimalField('Amount')
    measure29 = SelectField('Unit of Measurement', choices = [])
    amount30 = DecimalField('Amount')
    measure30 = SelectField('Unit of Measurement', choices = [])
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

    
    