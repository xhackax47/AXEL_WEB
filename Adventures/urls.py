from django.urls import path

from Adventures.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
