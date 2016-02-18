from django.contrib import admin

# Register your models here.

from .models import Day, Task



class TaskInLine(admin.StackedInline):
	model = Task
	extra = 3

class DayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),
        ('Day', {'fields': ['day'], 'classes': ['collapse']}),
        ('Daily goal',               {'fields': ['daily_goal']}),

    ]
    inlines = [TaskInLine]

admin.site.register(Task)
admin.site.register(Day, DayAdmin)
