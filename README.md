
- tidy up look of pages creating schedules
    amend shopping list needs looking at.
- error handling for incomplete recipes added, anc deleting recipes without ing or method
- display greeting message if no schedule set
- put dates on schedule?
- ability to select blank days

could it be deployed serverless?



need to:
-   ideally add ability to have two weeks of schedules (this week and next)
    - switch schedules at midnight Friday (delete this week and change id for next weeks)
    -  email schedule and shopping list. schedule emails url of each recipe each day


General

-  whe schedule is set, create timestamp, also store distance from timestamp to friday midnight. 
-  When login, or index is hit, calculate if timestamp & distance is in the past if so then 
-  make schedule1 = schedule2 and delete schedule 2. 
-  create prompt to create schedule 2.
-  search through database looking for recipes without a method, if found delete.

to deploy


Either python app.py to run locally, or docker build -t recipe_app:<version> and then 

docker run -d --name recipe-app --mount type=bind,source=/Users/michaelcorcoran/Documents/docker-mounts,target=/db -p 5050:5050 recipe-app:<version>