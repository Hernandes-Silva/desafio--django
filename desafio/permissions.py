from rest_framework import permissions
from django.contrib.auth.models import Group

class IsAdminOrReadOnlyViewSet(permissions.BasePermission):

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(request.method, view.action)
        
        if request.method in permissions.SAFE_METHODS:
            if view.action == 'create':
                return False

            return True

        group = Group.objects.get(name="admin_quiz")
        print(group in request.user.groups.all())

        return group in request.user.groups.all()   

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            return True

        group = Group.objects.get(name="admin_quiz")
        
        return group in request.user.groups.all()