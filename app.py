from application import app
from application import db
from application.models import Quantity, Method, Recipes, Cuisine, Ingredients, Schedule, Measure
from flask_sqlalchemy import inspect

inspector = inspect(db.engine)
if inspector.has_table == True:
    pass
else:
    db.create_all()

if Recipes.query.filter_by(recipe_name = 'Pea and Cauliflower Curry').first():
    pass
else:


    cuisines = ('Indian', 'Salad', 'Pasta', 'Various')
    for cus in cuisines:
        i = Cuisine(cus)
        db.session.add(i)
        db.session.commit()

    ingredients = ['sunflower oil', 'cumin seeds', 'brown mustard seeds', 'asafetida', 'cauliflower', 'turmeric', 'ground coriander', 'salt', 'sugar', 'frozen peas','medium tomato', 'fresh coriander', 'fresh green chillies','root ginger']
    for ing in ingredients:
        i = Ingredients(ing)
        db.session.add(i)
        db.session.commit()

    measures = ["ml", "g", "tsp", "tbsp", "whole", "large", "medium", "small", "cloves", "cm", "handful", "cup"]
    for m in measures:
        measure = Measure(m)
        db.session.add(measure)
        db.session.commit()

    rec = Recipes('Pea and Cauliflower Curry', 'quick and easy curry, no calorie details', 1)
    db.session.add(rec)
    db.session.commit()

    quantities = [ (1, 1,"",100.0,1),(1, 2,"", 1.0, 3), (1, 3,"", 1.0, 3), (1, 4,"", 0.5, 3), (1, 5,'cut into 1cm pieces', 1.0, 7), (1, 6,"", 1.0, 3) , (1, 7,"", 1.0, 4), (1, 8,"", 1.5, 3), (1, 9,"", 1.0, 3), (1, 10,"", 400.0, 2), (1, 11,"", 1.0, 7), (1, 12, 'roughly chopped', 1.0, 11), (1, 13,"", 4.0, 5),(1, 14, 'peeled and roughly chopped', 4.0, 10)]
    for q in quantities:
        quant = Quantity(*q)
        db.session.add(quant)
        db.session.commit()

    methods = [(1, 1, 'Crush the chillies and ginger together with a pinch of salt to make a fine masala paste'), (1, 2, 'Heat the oil in non-stick pan over a medium heat for 30s, then add the cumin and mustard seeds. When the mustard seeds start to pop reduce the heat and stir in teh asafetida '), (1, 3, 'Add the cauliflower and return the heat to medium. Stir in the masala paste, turmeric, ground coriander, salt, and sugar. Cover the pan and leave to cook for 8-10 minutes, stirring every few minutes.'), (1,4, 'stir in the peas and tomato and cook for a further 3-5 minutes'), (1,5, 'Remove from the heat and sprinkle with the chopped coriander. Leave for 5 minutes to let flavours develop')]
    for m in methods:
        met = Method(*m)
        db.session.add(met)
        db.session.commit()

    schedules =[(1,1,1,1), (2,1,1,1), (3,1,1,1), (4,1,1,1), (0,1,1,1)]
    for s in schedules:
        sched = Schedule(*s)
        db.session.add(sched)
        db.session.commit()
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)