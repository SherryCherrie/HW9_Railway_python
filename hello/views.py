from django.shortcuts import render
import random
import string
from .models import TimestampAndRandomString
from django.db import connection

# Create your views here.


def index(request):
    return render(request, "index.html")


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_timestamp_and_random_string (
                tick timestamp DEFAULT CURRENT_TIMESTAMP,
                random_string varchar(50)
            )
        """)

    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    new_record = TimestampAndRandomString(random_string=random_string)
    new_record.save()

    records = TimestampAndRandomString.objects.all().order_by('-tick')

    return render(request, "db.html", {"records": records})
