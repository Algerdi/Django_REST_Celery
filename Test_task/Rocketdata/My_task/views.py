from django.shortcuts import render
from .models import Position, Employee
from .serializers import EmployeeDetailSerializer, EmployeeListSerializer
from.permissions import *
from rest_framework import generics
from rest_framework.response import Response


# _________________________________________Вьюхи_______________________________________________

# Создание нового сотрудника
class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeDetailSerializer
    permission_classes = (IsGroupMember,)

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff == 1:
            return self.create(request, *args, **kwargs)
        else:
            emp = Employee.objects.filter(user_id=request.user.id)
            if len(emp) == 0:
                return self.create(request, *args, **kwargs)
            else:
                return Response(f'Вы не staff и у вас же есть созданный вами сотрудник - {emp.first().fio}')


# Просмотр всех сотрудников для стаффа и только себя для обычного смертного
class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsGroupMember,)

    def get_queryset(self):
        if self.request.user.is_staff == 1:
            return self.queryset.all()
        else:
            return self.queryset.filter(user_id=self.request.user.id)


# Редактирование, удаление данных сотрудника
# Здесь не ставил ограничения на просмотр/редактирование/удаление только себя, так как оно аналогично предыдущим
# и будет только мешать пониманию того как работает
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsGroupMember, IsOwnerOrReadOnly,)


# Просмотр одного сотрудника
# Здесь не ставил ограничения на просмотр только себя, так как оно аналогично предыдущим
# и будет только мешать пониманию того как работает
class EmployeeSingleListView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsGroupMember,)

    def get_queryset(self):
        return self.queryset.filter(emp_id=self.kwargs['emp_id'])


# Просмотр сотрудников по уровню
# Здесь не ставил ограничения на просмотр только себя, так как оно аналогично предыдущим
# и будет только мешать пониманию того как работает
class EmployeeLevelListView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Position.objects.all()
    permission_classes = (IsGroupMember,)

    def get_queryset(self):
        employees = []
        for i in self.queryset.filter(level=self.kwargs['level']):
            employees += list(Employee.objects.filter(pos__id=i.id))
        return employees


# _____________________________________________________________________________________________________________________




