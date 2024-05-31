# tentpole

Here are steps on how to run the tentpole assessment application
1. clone the code from https://github.com/Sheperd-Shikamaru/tentpole.git
2. create a vitual environment: python -m venv venv
3. activate the environment: venv\Scripts\activate
4. install project requirement: pip install -r requirements.txt
5. migrate the available tables to sqlite3: python manage.py migrate
6. create a superuser: python manage.py createsuperuser
7. run the server and login using superuser credentials: python manage.py runserver

For project documentation please open documentation folder to find user stories, ERD and workflow for the system