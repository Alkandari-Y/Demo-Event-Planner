from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users import views as auth_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.get_index, name='home'),
    path('auth/register/', auth_views.register_view, name='register'),
    path('auth/login/', auth_views.login_view, name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)