#base
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from .serializers import TaskSerializer

#inner
from .models import Task

# class CustomPermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user

class TaskView(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    #permission_classes = (CustomPermission,)

    def get_queryset(self):
        return Task.objects.all().order_by('-time_create')
