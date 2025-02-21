from rest_framework.permissions import BasePermission
class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.empoloyee.role == 'Admin' or obj.employee.user == request.user
                                                            