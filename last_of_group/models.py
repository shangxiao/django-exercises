from django.db import models


class Activity(models.Model):
    who = models.CharField(max_length=255)
    when = models.DateTimeField()
    what = models.CharField(max_length=255)
