import os
from celery import Celery
from celery.schedules import crontab
# import time
# from My_task.models import Employee



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rocketdata.settings')

app = Celery('Rocketdata')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'pay-salary-every-2-hours': {
        'task': 'main.tasks.pay_beat_salary',
        'schedule': crontab(),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# Здесь должно быть асинхронное удаление сотрудников, но у меня почему-то не видит My_task.models
# (ставил рут директорию Rocketdata и подчеркивание красное убиралось, но находить все равно не хочет)
# @app.task
# def zero(req):
#     time.sleep(1)
#     x = Employee.objects.filter(emp_id=req)
#     x.all_salary = 0
#     x.save()

