from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        else:
            return bool(request.user and request.user.is_staff)
    
    
class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        # check permissions for read_only request
        if request.method in permissions.SAFE_METHODS:
            return True

        # check permissions for write request
        else:
            return obj.review_user == request.user or request.user.is_staff 