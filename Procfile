web: gunicorn --config gunicorn.conf.py gettingstarted.wsgi

# web: gunicorn myproject.wsgi:application --bind 0.0.0.0:8080


# Uncomment this `release` process if you are using a database, so that Django's model
# migrations are run as part of app deployment, using Heroku's Release Phase feature:
# https://docs.djangoproject.com/en/6.0/topics/migrations/
# https://devcenter.heroku.com/articles/release-phase
release: ./manage.py migrate --no-input
