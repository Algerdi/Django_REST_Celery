from rest_framework import permissions
from django.contrib.auth.models import Group


# _________________________________________Пермишены___________________________________________________________________


# Либо владелец записи сотрудника и можешь редактировать, либо ты просто смотришь на выведенную информацию
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# Член группы или не член
class IsGroupMember(permissions.BasePermission):

    def has_permission(self, request, view):
        if len(Group.objects.filter(user=request.user.id)) != 0:
            if Group.objects.filter(user=request.user.id).first().name == 'PrimaryGroup':
                return True
            return False
        else:
            return False


# _____________________________________________________________________________________________________________________
