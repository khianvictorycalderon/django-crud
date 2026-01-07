# Django CRUD
Testing of Create, Read, Update, and Delete using SQLite as database.

## Setup
1. Clone this repository by running `git clone https://github.com/khianvictorycalderon/django-crud`
2. Create an `.env` file that contains:
    ```env
    DJANGO_SECRET_KEY="your-key-here"
    DEBUG=True
    ```
3. Run the following command for database migration:
    - `python manage.py makemigrations` or `py manage.py makemigrations`
    - `python manage.py migrate` or `py manage.py migrate`
4. To run the server, run `py manage.py runserver` or `python manage.py runserver`
    NOTE: If you encounter `Error: You don't have permission to access that port.`, just use a different port, for example:
    - `py manage.py runserver 8001`
    - `python manage.py runserver 8002`
    8001 and 8002 are the port.
5. To create another app, just run `python manage.py startapp <app-name>` or `py manage.py startapp <app-name>`, example: `py manage.py startapp myapp`

## Admin
1. To access the database using admin panel type in the url: "/admin"
2. Run `py manage.py createsuperuser` then enter the email, username, and password you want to use
3. You can edit your database now by logging in your account