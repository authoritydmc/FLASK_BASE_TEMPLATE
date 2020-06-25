import os
import sys
import subprocess
print("Welcome to Flask base Template Setup :) v 0.1")


def cmd(argument):
    print('*'*80)
    print('Argument->',argument)
    cmnd_stmt=list([str(x) for x in argument.split()])
    subprocess.call(cmnd_stmt)

    print('*'*80)
    input('Press enter to continue ')


project_name=str(input("Enter your project name please ->"))
project_name=project_name.lower().replace(' ','_')

parent_dir=os.path.join(os.getcwd(),project_name+"_root_directory")
project_dir=os.path.join(parent_dir,project_name)
print(parent_dir)


print("Setting up directories first ...")
try:
    os.makedirs(parent_dir)
    os.makedirs(project_dir)
    
except FileExistsError:
    print('root Directory already present..skipping it')

dir_list=['static','templates','routes','utility','databases']

for dir_name in dir_list:
    dir_path=os.path.join(project_dir,dir_name)
    try:
        os.makedirs(dir_path)
        print("Setting up ",dir_path)
    except FileExistsError:
        print(dir_path,'already exist ..skipping it')

print('done setting up directories...')



print('Setting up app.py')

with open (os.path.join(parent_dir,'app.py'),'w') as f:
    import_line=f"from {project_name} import app\n"
    main_line=r'if __name__ == "__main__":'
    run_line='\n    app.run()'

    f.write(import_line)
    f.write(main_line)
    f.write(run_line)


print('setting up __init __ file for main project ')

with open(os.path.join(project_dir,'__init__.py'),'w') as f:
    import_line='''from flask import  Flask\nfrom .routes import route1
    '''
    main_line='''\n\n\n\napp=Flask(__name__)\n\napp.register_blueprint(route1.bp)'''

    f.write(import_line)
    f.write(main_line)

print('setting up route1.py ')


route_path=os.path.join(project_dir,'routes')
with open(os.path.join(route_path,'route1.py'),'w') as f:
    import_line='from flask import render_template,redirect,url_for,Blueprint\n\n\n'

    main_line='''\nbp=Blueprint('route1',__name__)\n
    \n@bp.route('/')\ndef home():
        return render_template('base.html')\n'''

    f.write(import_line)
    f.write(main_line)


print('setting up base.html')

template_dir=os.path.join(project_dir,'templates')

with open(os.path.join(template_dir,'base.html'),'w')   as f:
    lines=f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Project: {project_name} </h1>
    <h2>Testing / route <h2>
    <h3> For management Guide goto <a href="https://authoritydmc.github.io/FLASK_BASE_TEMPLATE/" target="_blank">Here</a>

    <h4> Setup by <a href="github.com/authoritydmc">Authoritydmc </a>
</body>
</html>
    '''
    f.write(lines)


print('basic project done... Setting up Virtual Environment now...')
os.chdir(parent_dir)
print("Present Directory->")
cmd('pwd')

print('Installing pipenv')

cmd('pip3 install pipenv')




print('Installing Flask')
cmd('pipenv install flask')



print("After you enter in your virtual environment type flask run to test your program")
cmd('pipenv run flask run')


print('Activating the virtual environment using pipenv shell next time ')
cmd('pipenv shell')





