need to:
-   ideally add ability to have two weeks of schedules (this week and next)
    - schedule1/schedule2
    - when a schedule is created it gets an id 1 if no id 1, it gets id 2 if id 2 no schedule created.
    - shopping list also needs an id field. 
    - schedule needs to be either manual switch between the two (via js), or time limited with schedule 1 disappearing on the weekend, schedule 2 becoming schedule 1, and the same with shopping list.
    -  email schedule and shopping list. schedule emails url of each recipe 

write database schema
write website schema path


-   tidy up front end
-   make sure volume is persistent
-   write unit tests
-   make CI/CD pipeline
-   deploy on aws

Tasks to deploy to AWS

1. decide what services to use, i.e. eks, lightsail, ec2, lambda.
2. how to store the db, a container or redis
3. wht changes to be made to fit into service
4. improve front end look
5. fill db with recipes

pages



is what day is it used?

General

whe schedule is set, create timestamp, also store distance from timestamp to friday midnight. 
When login, or index is hit, calculate if timestamp & distance is in the past if so then 
make schedule1 = schedule2 and delete schedule 2. 
create prompt to create schedule 2.

Objects

sidebar = {
    week : (['list of recipe names from week'1]['list of recipe names from week2']),
    recipe_of_the_day : recipe_name(string)
    weekend : bolean
    day : ???
    user : username(string)
    shopping_list : ([list of ing tuples () for week1],[list of ing tuples() for week 2])
}
