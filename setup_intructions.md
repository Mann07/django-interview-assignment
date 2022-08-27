Python 3.8+

DATABASE SETUP:
project is using POSTGRES DATABASE to handle the data.
Download the postgresql 13.8 or greater.
    ->setup user name and password.
        Open the psql command-line tool:
            In the Windows Command Prompt, run the command:
                - psql -U userName
                - Enter your password when prompted.
    ->set portnumber : 8000
    -> run this command to download package which connects sql to django
        - pip install psycopg2
    -> open pgAdmin and create DATABASE as follow
        - name :'my_lib'
        - password : 'admin123'
        
    
Open cmd and go to the project directory/dnago-interview-assignment/library and run this commands:
    - pip install pipenv
    - pipenv shell
    - pipenv install django
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py collectstatic
    - python manage.py runserver

Open this link in Browser:  http://127.0.0.1:8000/login