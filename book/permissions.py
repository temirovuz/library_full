from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Admin uchun barcha ruxsatlar
        if request.user.is_authenticated and request.user.role == "admin":
            return True

        # Oddiy foydalanuvchilar uchun faqat o'qish huquqi
        return request.method in permissions.SAFE_METHODS
