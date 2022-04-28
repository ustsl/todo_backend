from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [

    #api
    path('api/v1', include('todo.urls')),

    #token
    path('user_auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    #base block
    path('admin/', admin.site.urls),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)