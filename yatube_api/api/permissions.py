from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthAuthor(BasePermission):
    """Пишем пользовательское разрешение."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
