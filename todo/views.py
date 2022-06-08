#base
from rest_framework import viewsets, permissions, views, response

#inner
from todo.serializers import TaskSerializer
from .models import Task

#views
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

#Получаем отдельным запросом почту юзера после авторизации. Необходимо для соответствующего поля на фронте

class GetUserData(views.APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        return response.Response({'email': str(self.request.user.email), 'is_staff': self.request.user.is_staff })