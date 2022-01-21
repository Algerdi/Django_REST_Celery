from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('employee/add/', EmployeeCreateView.as_view()),   # Создание нового сотрудника
    path('employee/all/', EmployeeListView.as_view()),   # Просмотр всех сотрудников для стаффа и только себя
    path('employee/single/<int:emp_id>/', EmployeeSingleListView.as_view()),   # Просмотр одного сотрудника
    path('employee/level/<int:level>/', EmployeeLevelListView.as_view()),   # Просмотр сотрудников по уровню
    path('employee/edit/<int:pk>/', EmployeeDetailView.as_view()),   # Редактирование данных сотрудника
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
