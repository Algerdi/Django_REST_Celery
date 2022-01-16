from __future__ import absolute_import, unicode_literals
from .models import Employee
from celery import shared_task
from celery.schedules import crontab


@shared_task()
def pay_beat_salary():
    print('Время начислять зарплату!')
    data = Employee.objects.all()
    for emp in data:
        emp.all_salary = float(emp.all_salary) + float(emp.salary_amount)
        emp.save()
