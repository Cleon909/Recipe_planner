from application import db
from application.models import Quantity, Method, Recipes, Cuisine, Ingredients

db.drop_all()
db.create_all()

cuisine1 = Cuisine('Curry')
db.session.add(cuisine1)
db.session.commit()
