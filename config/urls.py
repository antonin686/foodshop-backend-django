from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'Site administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', views.welcome),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)