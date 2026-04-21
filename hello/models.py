from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    
class TimestampAndRandomString(models.Model):
    tick = models.DateTimeField(auto_now_add=True)
    random_string = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'table_timestamp_and_random_string'