from django.contrib.admin.widgets import AdminDateWidget

from django import forms

from .models import Day, Task



class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('title', 'day', 'daily_goal')
        widgets = {
            'day': forms.DateInput(attrs={'class': 'datepicker'})
            }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('day',)
        labels = {
            'task_text': '',
        }
