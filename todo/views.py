#base
from rest_framework import viewsets, permissions, views, response

#inner
from todo.serializers import TaskSerializer
from .models import Task

#views
class TaskView(viewsets.ModelViewSet):
    #Единый блок для основных вьюх проекта

    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            if str(user) != 'AnonymousUser':
                serializer.save(user=user)
            else:   
                serializer.save()

        
class UserTaskView(TaskView):
    #Бизнес-логики немного - касается только фильтрации по параметрам. 
    # Думаю, нет смысла выносить бизнес-логику параметров в отдельный модуль

    def get_queryset(self):

        params = self.request.query_params.get
        sortingMethod = '-time_create'
        isDoneFilter = False

        if params('sorting'):
            sortingMethod = params('sorting')
        
        if params('is_done'):
            isDoneFilter = params('is_done')

        obj = Task.objects.filter(is_done=isDoneFilter)
        if params('get_mail') and '@' in params('get_mail'):
            obj = Task.objects.filter(is_done=isDoneFilter, user__email=params('get_mail'))
            
        return obj.order_by(sortingMethod)


class AdminTaskView(TaskView):
    #Административная вью для удобства обособлена от пользовательской вью, 
    # т.к. может предполагаться расширение методов. В принципе, можно также зашить в основную вью.

    permission_classes = [permissions.IsAdminUser]
    
    def get_queryset(self):
        return Task.objects.all()



class GetUserData(views.APIView):
    #Получаем отдельным запросом почту юзера после авторизации. 
    # Необходимо для соответствующего поля на фронте

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        return response.Response({'email': str(self.request.user.email), 'is_staff': self.request.user.is_staff })