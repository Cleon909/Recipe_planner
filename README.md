
- error handling for incomplete recipes added
- display greeting message if no schedule set
- put dates on schedule?
- ability to select blank days
- make it mobile friendly

could it be deployed serverless?

to deploy


Either python app.py to run locally, or docker build -t recipe_app:<version> and then 

docker run -d --name recipe-app --mount type=bind,source=/Users/michaelcorcoran/Documents/docker-mounts,target=/db -p 5050:5050 -e GMAIL=<password> recipe-app:<version>