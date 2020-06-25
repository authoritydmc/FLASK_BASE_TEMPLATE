# FLASK_BASE_TEMPLATE



## Structure Explanation and format

### root directory will have : 

  **app.py** will be the file which will run by flask run or guniorn app:app

  **application** pacakage will contain all the source code related to your project

  **other setup files** like gitignore ,Procfile,lockfiles etc ...
 
### application directory will have :-  

  **__init__.py** file has Flask app object ,here you will register you **Blueprint** for different routing modules of your project


  **each Subdirectories(subpackages) are used to distinctly code and manage the system. so the project doesnt become a mess.**


  **databases** <subdirectory  :-  will contain module related to your databases functionality

 **routes** <subdirectory  :-   will contain all the different sub routing modules ..

 **utility** <subdirectory  :-   will contain utitlity modules  like sending email , making a random ID generation module ..

 **static** <subdirectory  :-   will contain static files like css ,javascripts ,images etc.

 **templates** <subdirectory  :-    wil contain jinja based layout for web page creation ..
  

## Working With Template <Guide>

 
 ### Prerequisite:
 1. Install **pipenv** for virtual environment management of this project
  > to do so : open **terminal** type `pip install pipenv` 
  **NOTE pip should be pip3 incase u have both python2 and python3 already installed**
 
 
  
 ### Steps

 #### Installation {first time only }
 1. First Click on **Use this Template** button given above.
 2. Create a new repository in your account with whatever name you want.
 3. Now Git clone your repository to your local machine..
 4. Goto cloned repo's directory on your local machine and type **`pipenv install` **
  > it will make a virtual environment inside the directory and also if a requirements.txt file is present ,it will try to install all the mentioned requirement
 
 
 #### CODING AND RUNNING YOUR WEBAPP
 
 1. now whenever you want to work on this project ..always open the **terminal** at the directory path 
 2. Type **pipenv shell** to activate virtual Environment
 3. If you need any python module ..**INSTEAD OF INSTALLING WITH pip install :modulename: use pipenv install :modulename:
 4. use **flask run** or install gunicorn and run the app with gunicorn app:app
 
 
 
