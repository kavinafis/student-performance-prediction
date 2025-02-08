from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    study_hours = models.FloatField()
    previous_scores = models.FloatField()
