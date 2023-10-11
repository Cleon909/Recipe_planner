
- put dates on schedule?
- ability to select blank days
- make it mobile friendly
- tasks
    - delete user
    
#
to deploy

Locally

need to set env variables:

DATABASE_URI = location of database to be used. 
SECRET_KEY = random string
GMAIL = password for recipeapp909 gmail account

then run python app.py

to build and deploy docker image

docker build -t recipe_app:<version> and then 

docker run -d --name recipe-app --mount type=bind,source=/Users/Public/docker-mounts,target=/db -p 5050:5050 -e GMAIL=<password> -e DATABASE_URI=<database_uri> -e SECRET_KEY=<key> recipe_app:<version>