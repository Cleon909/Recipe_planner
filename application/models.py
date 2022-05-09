from enum import unique
from application import db

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(50), nullable=False, index=True, unique=True)
    quantity = db.relationship("Quantity", backref="ingredients")
    shoppinglist = db.relationship("ShoppingList", backref="shopping_list")


    def __init__(self, ingredient_name):
        self.ingredient_name = ingredient_name

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(50), nullable=False)
    recipe = db.relationship('Recipes', backref='cuisine')

    def __init__(self, cuisine_name):
        self.cuisine_name = cuisine_name

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    recipe_description = db.Column(db.String(500))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.id'))
    quantity = db.relationship('Quantity', backref="recipes")
    method = db.relationship('Method', backref='mrecipes')


    def __init__(self, recipe_name, recipe_description, cuisine_id):
        self.recipe_name = recipe_name
        self.recipe_description = recipe_description
        self.cuisine_id = cuisine_id

class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
    ingredient_prep = db.Column(db.String(100))
    amount = db.Column(db.Float, nullable=False)
    measure = db.Column(db.Integer, db.ForeignKey('measure.id'))


    def __init__(self, recipe_id, ingredient_id, ingredient_prep, amount, measure):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.ingredient_prep = ingredient_prep
        self.amount = amount
        self.measure = measure

class Method(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    step_num = db.Column(db.Integer, nullable=False)
    step = db.Column(db.String(200), nullable=False)

    def __init__(self, recipe_id, step_num, step):
        self.recipe_id = recipe_id
        self.step_num = step_num
        self.step = step

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_the_week = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    def __init__(self, day_of_the_week, recipe_id):
        self.recipe_id = recipe_id
        self.day_of_the_week = day_of_the_week

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measure = db.Column(db.String(20), nullable=False, index=True, unique=True)
    quantity = db.relationship("Quantity", backref="measurebr")
    shoppinglist = db.relationship("ShoppingList", backref="measurebr1")

    def __init__(self, measure):
        self.measure = measure

class ShoppingList(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False, index=True)
    amount = db.Column(db.Float, nullable=False)
    measure_id = db.Column(db.Integer, db.ForeignKey('measure.id'), nullable = False)

    def __init__(self, ingredient_id, amount, measure_id):
        self.ingredient_id = ingredient_id
        self.amount = amount
        self.measure_id = measure_id


