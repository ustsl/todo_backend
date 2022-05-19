#base
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from .serializers import TaskSerializer

#inner
from .models import Task



class TaskView(viewsets.ModelViewSet):

    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            if str(user) != 'AnonymousUser':
                serializer.save(user=user)
            else:   
                serializer.save()

        
class ActiveTask(TaskView):

    def get_queryset(self):
        return Task.objects.filter(is_done=False).order_by('-time_create')

class ArchiveTask(TaskView):
    
    def get_queryset(self):
        return Task.objects.filter(is_done=True).order_by('-time_create')
