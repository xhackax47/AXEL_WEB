from django.urls import path, include
from rest_framework import routers

from api.views import DocumentListViewSet, DocumentDetailView, DataSetDetailView, RobotDetailView, DataSetListViewSet,\
    RobotListViewSet

app_name = 'api'

# Routage des différentes listes
router = routers.DefaultRouter()
router.register('documents', DocumentListViewSet, 'documents')
router.register('datasets', DataSetListViewSet, 'datasets')
router.register('robots', RobotListViewSet, 'robots')

urlpatterns = [

    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('document/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('dataset/<int:pk>/', DataSetDetailView.as_view(), name='dataset-detail'),
    path('robot/<int:pk>/', RobotDetailView.as_view(), name='robot-detail'),
]
