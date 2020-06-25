# FLASK_BASE_TEMPLATE


# USING THIS TEMEPLATE

## Structure Explanation and format

### root directory will have :>

> **app.py** will be the file which will run by flask run or guniorn app:app

> **application** pacakage will contain all the source code related to your project

> **other setup files** like gitignore ,Procfile,lockfiles etc ...
 
### application directory will have :-> 

> **__init__.py** file has Flask app object ,here you will register you **Blueprint** for different routing modules of your project


> **each Subdirectories(subpackages) are used to distinctly code and manage the system. so the project doesnt become a mess.**


> **databases** <subdirectory> :-> will contain module related to your databases functionality

>**routes** <subdirectory> :->  will contain all the different sub routing modules ..

>**utility** <subdirectory> :->  will contain utitlity modules  like sending email , making a random ID generation module ..

>**static** <subdirectory> :->  will contain static files like css ,javascripts ,images etc.

>**templates** <subdirectory> :->   wil contain jinja based layout for web page creation ..
  

