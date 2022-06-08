
from django.urls import path
from .views import *

urlpatterns = [
    path('', ActiveTask.as_view({'post': 'create', 'get': 'list'})),
    path('archive/', ArchiveTask.as_view({'get': 'list'})),
    path('get_user/', GetUserData.as_view()),
    path('<int:pk>/', AllTask.as_view({'put': 'update'})),
]
