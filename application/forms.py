from socket import AI_ALL
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SelectField, SubmitField, PasswordField, DecimalField, FormField, BooleanField, TextAreaField, FieldList, EmailField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from application.models import ShoppingList, User


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
    sched_no = SelectField('Schedule for this week or next', choices = [(1, 'Next week'), (0, 'This week')])
    submit_cuisine = SubmitField('Generate Recipe Schedule')
    
class DeleteRecipeForm(FlaskForm):
    recipe = SelectField('Select Recipe to Delete', choices = [])
    submit = SubmitField('press to Delete')
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

class AmountForm(FlaskForm):
    amount = DecimalField("  ")
class AmendAmountForm(FlaskForm):
    ingredients = FieldList(FormField(AmountForm))
    submit = SubmitField("press to amend shopping list")
   
class PostShoppingListForm(FlaskForm):
    email = EmailField("enter additional email address for shopping list")
    submit = SubmitField("press to email shopping list")


class IngredientForm(FlaskForm):
    ingredient = SelectField('Choose Ingredient', choices = [])
    ingredient_alt = StringField('If ingredient not in list type here', validators = [Length(max = 50)], default = "")
    amount = DecimalField('Amount')
    measure = SelectField('Unit', choices = [])
    ingredient_prep = StringField('chopped, sliced etc. Leave blank if no prep needed', validators = [Length(max=100)])
    
class MethodForm(FlaskForm):
    method = StringField('Input method of making the recipe in steps', validators = [Length(max=300)], default = "")

class AddRecipeForm1(FlaskForm):
    name = StringField('Name of Recipe', validators = [DataRequired(), Length(max = 200)])
    recipe_description = TextAreaField('Details of recipe(i.e. cooking time, calories, macros etc', render_kw={'rows':4}, validators = [(Length(max = 500))])
    cuisine = SelectField('Type of Cuisine', choices = [])
    no_ingredients = IntegerField('Add number of ingredients (ingredient details added on next page)')
    no_method_steps = IntegerField('Add number of method steps')
    submit = SubmitField('Press to add recipe')
    
class AddRecipeForm2(FlaskForm):    
    ingredients = FieldList(FormField(IngredientForm))
    methods = FieldList(FormField(MethodForm))
    submit = SubmitField('Press to add ingredients and method steps')

class LoginForm(FlaskForm):
    username = StringField('input username', validators = [DataRequired()])
    password = StringField('input password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

