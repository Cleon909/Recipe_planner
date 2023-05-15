from flask_login import current_user, login_user, logout_user, login_required
from application.models import Ingredients, Cuisine, Recipes, Quantity, Method, Schedule, Measure, ShoppingList, User
import calendar
from datetime import date, datetime
import os
from application import db
import smtplib


# this function gets the recipe for each day, filters by day and logged in user id
def get_recipe_for_day(day_number, week_n):
    if current_user.is_authenticated:
        id = Schedule.query.filter_by(day_of_the_week = day_number, user_id = current_user.id, sched_no = week_n).first()
        if id is not None:
            day_recipe = Recipes.query.filter_by(id = id.recipe_id).first()
            return day_recipe
        # else:
        #     return Recipes.query.filter_by(id = 1).first()

# this function assembles the recipe for each day adding it to a list in order of the days to be used in the layout template
def get_weekly_recipes():
    week, week2 = [], []
    for num in range(5):
         week.append(get_recipe_for_day(num, 1))
    for num in range(5):
         week2.append(get_recipe_for_day(num, 2))
    return (week, week2)

# check if current user already has a schedule set
def check_for_schedule():
    if Schedule.query.filter_by(user_id = current_user.id, sched_no = 1).first() is None:
        return False
    return True

#this function grabs the recipe for the individual day (filtering by day and user id) to be used in the layour template 
def get_recipe_of_the_day():
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        recipe_of_the_day = "It's the weekend, do your own thing"
    else:
        recipe_of_the_day = Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = datetime.today().weekday(), user_id = current_user.id, sched_no = 1).first().recipe_id).first().recipe_name
    return recipe_of_the_day

# check if it's a weekend
def weekend_or_not():
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        weekend = True
    else:
        weekend = False
    return weekend

def what_day_is_it():
    day = date.today()
    day = calendar.day_name[day.weekday()]
    return day

# this cycles through the shopping list picks out the relevant items (filtered by user id), grabbing the data from other tables and puts it into a list of lists with relevant details. 
def create_shopping_list():
    shopping_list_raw1 = ShoppingList.query.filter_by(user_id = current_user.id, sched_no = 1).all()
    shopping_list1 = []
    for shopping_list_raw_item in shopping_list_raw1:
        shopping_list1.append([Ingredients.query.filter_by(id=shopping_list_raw_item.ingredient_id).first().ingredient_name, shopping_list_raw_item.amount, Measure.query.filter_by(id = shopping_list_raw_item.measure_id).first().measure])
    shopping_list_raw2 = ShoppingList.query.filter_by(user_id = current_user.id, sched_no = 2).all()
    shopping_list2 = []
    for shopping_list_raw_item in shopping_list_raw2:
        shopping_list2.append([Ingredients.query.filter_by(id=shopping_list_raw_item.ingredient_id).first().ingredient_name, shopping_list_raw_item.amount, Measure.query.filter_by(id = shopping_list_raw_item.measure_id).first().measure])
    return (shopping_list1, shopping_list2)

# function to delete this weeks's schedule and change next week to this week
def switch_schedules():
    all_users = User.query.all()
    for user in all_users:
        schedules_to_delete = Schedule.query.filter_by(user_id = user.id, sched_no = 1).all()
        for schedule in schedules_to_delete:
            db.session.delete(schedule)
            db.session.commit()
        schedules_to_switch = Schedule.query.filter_by(user_id = user.id, sched_no = 2).all()
        for schedule in schedules_to_switch:
            schedule.sched_no = 1
            db.session.add(schedule)
            db.session.commit()
        ing_to_delete = ShoppingList.query.filter_by(user_id = user.id, sched_no = 1).all()
        for ing in ing_to_delete:
            db.session.delete(ing)
            db.session.commit()
        ing_to_switch = ShoppingList.query.filter_by(user_id = user.id, sched_no = 2).all()
        for ing in ing_to_switch:
            ing.sched_no = 1
            db.session.add(ing)
            db.session.commit() 

def post_recipe():
    gmail_user = "recipeapp909@gmail.com"
    gmail_password = os.environ['GMAIL']
    sent_from = gmail_user
    all_users = User.query.all() 
    for user in all_users:
        recipe_of_the_day = Recipes.query.filter_by(id = Schedule.query.filter_by(day_of_the_week = datetime.today().weekday(), user_id = user.id, sched_no = 1).first().recipe_id).first()
        to = [user.email]
        print(f"{recipe_of_the_day.method}")
        subject = 'Recipe of the Day'
        body =  "Today's Recipe is\n\n"
        body += f"{recipe_of_the_day.recipe_name}\n"
        body += f"Description\n"
        body += f"{recipe_of_the_day.recipe_description}\n"
        body += f"Method\n"
        body += f"{Method.query.filter_by(recipe_id=recipe_of_the_day.id).first().step}\n"

    email_text= "from:{}\nto:{}\nsubject:{}\n{}".format(sent_from, ",".join(to),subject,body)
    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user,gmail_password)
        smtp_server.sendmail(sent_from,to,email_text)
        smtp_server.close()
    except Exception as ex:
       print(ex)

def clean_database():
    recipes_to_delete = Recipes.query.filter(Recipes.method == None).all()
    for recipe in recipes_to_delete:
        db.session.delete(recipe)
        db.session.commit()

