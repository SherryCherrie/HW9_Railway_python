from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    random_string = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Read from DB at {self.when} - {self.random_string}"
