# Django CRUD
Testing of Create, Read, Update, and Delete using SQLite as database.

## Setup
1. Clone this repository by running `git clone https://github.com/khianvictorycalderon/django-crud`
2. Create an `.env` file that contains:
    ```env
    DJANGO_SECRET_KEY="your-key-here"
    DEBUG=True
    ```
3. To run the server, run `py manage.py runserver` or `python manage.py runserver`
    NOTE: If you encounter `Error: You don't have permission to access that port.`, just use a different port, for example:
    - `py manage.py runserver 8001`
    - `python manage.py runserver 8002`
    8001 and 8002 are the port.