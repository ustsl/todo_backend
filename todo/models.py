from django.db import models
from django.conf import settings

# Create your views here.

class Task(models.Model):

    #Модель связана с юзером. Содержит в себе поля тасков
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='data_user',
                                verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    #Контент задачи (тайтл по ТЗ не требуется, но на всякий случай вывел и его)
    title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок задачи")
    content = models.TextField(blank=True, verbose_name="Описание задачи")

    #Рабочие
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    is_done = models.BooleanField(default=False, verbose_name="Сделано")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def get_mail(self):
        #В модели храним получение мэйла юзера
        if self.user:
            return self.user.email
        return 'anonymous'

    def __str__(self):
        return self.title
