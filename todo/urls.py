
from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskView.as_view({'put': 'create', 'get': 'list'})),
]
