from rest_framework import serializers
from .models import Task

class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("pk", "user", "title", "content", "time_create", "is_done", "get_mail")

        