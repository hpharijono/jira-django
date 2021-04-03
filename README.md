# jira-django

Jira clone API using Django and Django REST Framework

## Setup
1. Clone the project repository
   ```commandline
   git clone https://github.com/hpharijono/jira-django.git
   ```
2. Create and activate a virtual environment
   ```commandline
   virtualenv env
   source env/bin/activate
   ```
3. Install requirements
    ```commandline
    pip install -r requirements.txt
    ```
4. Configure your Postgres database in DATABASES variable in jira/settings.py file
    ```commandline
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "jira",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    ```
5. Create User
    ```commandline
    python manage.py createsuperuser
    ```

6. Load fixtures
    ```commandline
    python manage.py loaddata projects
    python manage.py loaddata tickets
    ```

7. Run application
   ```commandline
   python manage.py runserver
   ```
   
## Run tests
   ```commandline
   pytest .
   ```

## API Documentation
```commandline
http://localhost:8000/api-docs/
```
