# django-docker-base
Quickly setup a new django env with docker

## Credits to this blog post and video

[ockerized-django-app-with-vscode](https://londonappdeveloper.com/debugging-a-dockerized-django-app-with-vscode/)

## Process to recreate entirely.

#### Create the Django project

1. add .gitignore from Github 

[python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

2. Create the app directory for the django project

```bash
mkdir app
```

3. Run the singular Docker command to install django and create the project

```bash
docker run -v ${PWD}/app:/app -w /app python:3.9-alpine sh -c "pip install Django==3.2 && django-admin startproject app ."
```

After this all project files under app should appear

In next section we will create the docker config to easily run the Django webserver.

#### Create the docker config

Before you continue, note that this process will create the following files in your project, replacing them if they already exist:

- requirements.txt
- Dockerfile
- docker-compose.yml
- docker-compose.debug.yaml
- .vscode/launch.json
- .vscode/tasks.json

Use the docker extension to add the settings files

1. Open the VScode command pallet

```
macOS: CMD + SHIFT + P
Windows: CTRL + SHIFT + P
``` 

2. Choose 'Docker: Add Docker Files to Workspace.'

3. On the Select Application Platform prompt, locate Python: Django and select it:

4. On the Choose the app’s entry point prompt, select app/manage.py and select it:

5. Leave the port as 8000 and answer Yes to create the 'docker-compose.yml' file 

6. Change the docker files that were created in MAC to LF at the bottom in VS code.

7. Update the requirments.txt to be more specific

```   
django>=3.2,<3.3
gunicorn>=20.0.4,<20.1
```

8. Update the Dockerfile like so


- Changed base image to python:3.9-alpine3.13 because it is more lightweight.
- Changed the COPY . /app command to COPY /app /app so only our Django app is copied into the Docker image.
- Modified the gunicorn command to use the app.wsgi file for running our app.

9. Build the Django webserver and run

```
docker-compose build
docker-compose up
```
 
#### Debugging tools through Docker

Next open the compose file for django debugging.

1. Locate the app/manage.py line and remove the app/ to change it to manage.py.

We make this change because our container is already working from the app/ directory, so we can call the manage.py file directly.

2. Next we need to make some changes on the .vscode folder that was created earlier.

Next open up .vscode/launch.json, locate the line "localRoot": "${workspaceFolder}", and replace it with "localRoot": "${workspaceFolder}/app",.

Again, this change is because our Django project is going to be stored within /app instead of the root project.



3. Open the tasks.json file and make small alteration

Open up .vscode/tasks.json and change "file": "app/manage.py" to "file": "manage.py".


#### Next test out the debugger by creating simple view in Django

1. Create views.py file alongside urls.py

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World!')
```

2. Update the urls.py

```python
from django.contrib import admin
from django.urls import path

from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
```

### Now you can start to use the Debgger in VS code.

While the backend is running via docker.

Select Run start debugging in VScode.

You can then access the debugging varialbes in the debug console in VScode.


## The application is extended to give example of the rest API

to check this working run the server and navigate to 

`http://localhost:8000/api/hello-world/items/`

alternatively you can use `CURl` command

## Running commands in django

The Django commands (`migrate`, `create_admin` and `create_groups`) can be run in the container directly:

```bash
docker-compose exec webapp python manage.py <COMMAND>
``` 

This way you can create an admin user to help manage the celery tasks for example

To get the API to work you need to migrate

```bash
docker-compose -f docker-compose.yml exec webapp python manage.py migrate
```