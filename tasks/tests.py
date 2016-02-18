from django.test import TestCase

from .models import Day

class NewDayTest(TestCase):

    def test_new(self):
        self.client.post('/tasks/new/', data={'day':'2016-12-04'})
        Day.objects.get(day='2016-12-04')

    def test_new_with_tasks(self):
        self.client.post('/tasks/new/', data={'day':'2016-12-04','0-task_text':'task1', '1-task_text':'task2'})
        day = Day.objects.get(day='2016-12-04')
        tasks = day.task_set.all()
        self.assertEqual(len(tasks), 2)

class EditDayTest(TestCase):

    def test_edit(self):
        day = Day.objects.create(day='2016-12-04')
        self.client.post('/tasks/%s/edit/' % day.id, data={'day':'2016-12-05'})
        self.assertEqual(str(Day.objects.get(id=day.id).day), '2016-12-05')

    def test_edit_add_task(self):
        day = Day.objects.create(day='2016-12-04')
        self.client.post('/tasks/%s/edit/' % day.id, data={'day':'2016-12-05', '0-task_text':'task1', '1-task_text':'task2'})
        self.assertEqual(len(Day.objects.get(id=day.id).task_set.all()), 2)
