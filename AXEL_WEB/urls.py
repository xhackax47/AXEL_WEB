from django.contrib import admin
from django.urls import path, include

from WebAXEL.views import ConstructionView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('adminAXEL/', include('AdminAXEL.urls')),
    path('adminAXEL/', ConstructionView.as_view(), name='construction'),
    path('adventures/', include('Adventures.urls')),
    path('api/v1/', include('api.urls')),
    path('', include('WebAXEL.urls')),
]
