from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model


User = get_user_model()

# _________________________________________________Модель для должностей_______________________________________________

# Можем создавать должности, чтобы потом выдавать их сотрудникам в админке
class Position(MPTTModel):
    name = models.CharField(max_length=50, unique=False,  verbose_name='Должность')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',  verbose_name='Руководитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    class MPTTMeta:
        order_insertion_by = ['name']

# _____________________________________________________________________________________________________________________


# _________________________________________________Модель для сотрудников_______________________________________________


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True, verbose_name='Номер')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    pos = TreeForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    hired_at = models.DateField(auto_now_add=False, verbose_name='Дата приема на работу')
    salary_amount = models.FloatField(default=0, verbose_name='Размер ЗП')
    all_salary = models.FloatField(default=0, verbose_name='Выплачено ЗП')
    user = models.ForeignKey(User, verbose_name='Созд. пользователь', on_delete=models.CASCADE)

    def pos_name(self):
        return self.pos.name
    pos_name.short_description = 'Должность'

    def pos_level(self):
        return self.pos.level
    pos_level.short_description = 'Уровень'

    def pos_parent(self):
        dol = self.pos.get_ancestors(ascending=True, include_self=False)
        boss = Employee.objects.filter(pos=dol.first())
        return f'{boss.first()} - {dol.first()}' if dol else 'Сам себе голова'
    pos_parent.short_description = 'Руководитель'

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['emp_id']


# _____________________________________________________________________________________________________________________












