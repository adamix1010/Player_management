from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import landing_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('', landing_page, name='landing-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

