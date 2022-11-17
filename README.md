need to:
-   ideally add ability to have two weeks of schedules (this week and next)
    - schedule1/schedule2
    - when a schedule is created it gets an id 1 if no id 1, it gets id 2 if id 2 no schedule created.
    - shopping list also needs an id field. 
    - schedule needs to be either manual switch between the two (via js), or time limited with schedule 1 disappearing on the weekend, schedule 2 becoming schedule 1, and the same with shopping list.
    -  email schedule and shopping list. schedule emails url of each recipe 

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