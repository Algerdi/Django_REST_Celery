from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Position, Employee
# from Rocketdata.celery import zero


# Команда для "обнуления" ;) зарплат выделенных сотрудников
# Здесь должно быть асинхронное удаление сотрудников, но у меня почему-то не видит My_task.models
# (ставил рут директорию Rocketdata и подчеркивание красное убиралось, но находить все равно не хочет)
@admin.action(description='Обнулить выплаченные зарплаты')
def make_zero(modeladmin, request, queryset):
    if len(queryset) > 20:
        queryset.update(all_salary=0)
        # for person in queryset:
        #     zero.delay(person.emp_id)
    else:
        queryset.update(all_salary=0)

# _________________________________________Регистрация модели должностей_______________________________________________


# admin.site.register(Position, MPTTModelAdmin)
admin.site.register(
    Position,
    DraggableMPTTAdmin,
    list_display=('id',
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

# _____________________________________________________________________________________________________________________


# _________________________________________Регистрация модели сотрудников_______________________________________________


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fio', 'pos_name', 'salary_amount', 'all_salary', 'pos_level', 'pos_parent', 'user')
    list_display_links = ('fio', 'pos_name',)
    search_fields = ('fio', 'pos__name',)
    list_filter = ('pos__name', 'pos__level',)
    readonly_fields = ('all_salary', 'pos_parent',)
    # list_editable = ('all_salary',)
    actions = [make_zero]

admin.site.register(Employee, EmployeeAdmin)

# _____________________________________________________________________________________________________________________

# Изменения названия тайтла и хедера
admin.site.site_title = 'Атпути ИНКОРПАРЕЙТЕД'
admin.site.site_header = 'Атпути ИНКОРПАРЕЙТЕД'



