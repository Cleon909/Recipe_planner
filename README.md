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

home page
recipe of the day has to show recipe from week 1

Amend shopping list
both shopping lists are now posted to front end, change to handle
needs ability to switch between weeks to amend? 


post shopping list
both shopping lists are now posted to front end, change to handle

ability to choose which week list to post. 

layout 
make sidebar recipes show week 1, 

General
write database schema
write website schema path
function to move week 2 schedule to week1 and delete week 2.
    - will function move on a particular date, if date is missed?
    - maybe it switches if it's after the first friday from setting the schedule

add sheet to show schedule and shopping list for each week, switch between weeks through JS.
Will need to send both weeks to page. 