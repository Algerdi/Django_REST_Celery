from rest_framework import serializers
from .models import *


# _________________________________________Сериалайзеры________________________________________________________________


# Создаем или редактируем сотрудника
class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Employee
        fields = '__all__'


# Выводим сотрудника
class EmployeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('emp_id', 'fio', 'pos_name', 'hired_at', 'salary_amount', 'all_salary', 'pos_level', 'pos_parent',)


# _____________________________________________________________________________________________________________________




