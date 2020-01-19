from django.contrib import admin
from django.urls import path, include

from WebAXEL import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminAXEL/', include('AdminAXEL.urls')),
    path('api/v1/', include('api.urls')),
    path('', include('WebAXEL.urls')),
]