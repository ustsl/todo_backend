
from django.urls import path
from .views import *

urlpatterns = [
    path('', UserTaskView.as_view({'post': 'create', 'get': 'list'})),
    path('get_user/', GetUserData.as_view()),
    path('<int:pk>/', AdminTaskView.as_view({'put': 'update'})),
    path('<int:pk>/delete', AdminTaskView.as_view({'put': 'destroy'})),
]
