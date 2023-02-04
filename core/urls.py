from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shared import views as shared_views
from users import views as user_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.get_index, name='home'),
    path("events/create/", event_views.event_create_view, name="event_create"),
    path("events/<int:event_id>/", event_views.event_detail_view, name="event_detail"),
    path("events/<int:event_id>/update/", event_views.event_update_view, name="event_update"),
    path("events/<int:event_id>/delete/", event_views.event_delete_view, name="event_delete"),
    path('accounts/register/', user_views.register_view, name='register'),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/logout/', user_views.logout_view, name='logout'),
    path('access-denied/', shared_views.access_denied_view, name='unauthorized'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)