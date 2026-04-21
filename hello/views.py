from django.shortcuts import render

from .models import Greeting

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

    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    greeting = Greeting()
    greeting.random_string = random_string
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
