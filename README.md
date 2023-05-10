need to:
-   ideally add ability to have two weeks of schedules (this week and next)
    - switch schedules at midnight Friday (delete this week and change id for next weeks)
    -  email schedule and shopping list. schedule emails url of each recipe 

-   tidy up front end
-   change method to text area.
-   write unit tests
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

to deploy

docker run -d --name recipe-app --mount type=bind,source=/Users/michaelcorcoran/Documents/docker-mounts,target=/db -p 5050:5050 recipe-app:v1.0.5