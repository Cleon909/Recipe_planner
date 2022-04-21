from application import db
from application.models import Quantity, Method, Recipes, Cuisine, Ingredients, Schedule

db.drop_all()
db.create_all()

cuisine1 = Cuisine('Curry')
db.session.add(cuisine1)
db.session.commit()

cuisine1 = Cuisine('Salad')
db.session.add(cuisine1)
db.session.commit()

cuisine1 = Cuisine('Pasta')
db.session.add(cuisine1)
db.session.commit()

cuisine1 = Cuisine('Various')
db.session.add(cuisine1)
db.session.commit()

ingredients = ['sunflower oil', 'cumin seeds', 'brown mustard seeds', 'asafetida', 'cauliflower', 'turmeric', 'ground coriander', 'salt', 'sugar', 'frozen peas','medium tomato', 'fresh coriander', 'fresh green chillies','root ginger']
for ing in ingredients:
    i = Ingredients(ing)
    db.session.add(i)
    db.session.commit()

rec = Recipes('Pea and Cauliflower Curry', 'quick and easy curry, no calorie details', 1)
db.session.add(rec)
db.session.commit()

quantities = [ (1, 1,"",100.0, 'ml'),(1, 2,"", 1.0, 'tsp'), (1, 3,"", 1.0, 'tsp'), (1, 4,"", 0.5, 'tsp'), (1, 5,'cut into 1cm pieces', 1.0, 'medium'), (1, 6,"", 1.0, 'tsp'), (1, 7,"", 1.0, 'tbp'), (1, 8,"", 1.5, 'tsp'), (1, 9,"", 1.0, 'tsp'), (1, 10,"", 400.0, 'grams'), (1, 11,"", 1.0, 'medium'), (1, 12, 'roughly chopped', 1.0, 'handful'), (1, 13,"", 4.0, 'whole'),(1, 14, 'peeled and roughly chopped', 4.0, 'cm')]
for q in quantities:
    quant = Quantity(*q)
    db.session.add(quant)
    db.session.commit()

methods = [(1, 1, 'Crush the chillies and ginger together with a pinch of salt to make a fine masala paste'), (1, 2, 'Heat the oil in non-stick pan over a medium heat for 30s, then add the cumin and mustard seeds. When the mustard seeds start to pop reduce the heat and stir in teh asafetida '), (1, 3, 'Add the cauliflower and return the heat to medium. Stir in the masala paste, turmeric, ground coriander, salt, and sugar. Cover the pan and leave to cook for 8-10 minutes, stirring every few minutes.'), (1,4, 'stir in the peas and tomato and cook for a further 3-5 minutes'), (1,5, 'Remove from the heat and sprinkle with the chopped coriander. Leave for 5 minutes to let flavours develop')]
for m in methods:
    met = Method(*m)
    db.session.add(met)
    db.session.commit()

schedules =[(1,1), (2,1), (3,1), (4,1), (0,1)]
for s in schedules:
    sched = Schedule(*s)
    db.session.add(sched)
    db.session.commit()
