from django.db import models
from datetime import datetime    


class Day(models.Model):

    title = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    day = models.DateField(unique=True, default=datetime.now)
    daily_goal = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.task_text