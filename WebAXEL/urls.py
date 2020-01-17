from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

# app_name = 'WebAXEL'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Inscription
    path('register/', views.RegisterView.as_view(), name='register'),
    # Authentification
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Internationalisation
    path('i18n/', include('django.conf.urls.i18n')),
    # Index
    path('home/', login_required(views.HomeView.as_view()), name='home'),
    # Gestion de compte par username
    url(r'^account-settings/(?P<username>\w+)/$', login_required(views.AccountSettingsView.as_view()),
         name='account-settings'),

    # Details Document
    path('document/<int:pk>', login_required(views.DocumentView.as_view()), name='document'),
    # Liste Documents
    path('documents', login_required(views.DocumentsView.as_view()), name='documents'),
    # Chercher Documents
    path('document-search', login_required(views.DocumentSearchResultsView.as_view()), name='document-search-results'),
    # Creer Document
    path('create-document', login_required(views.DocumentCreateView.as_view()), name='create-document'),
    # Modifier Document
    path('edit-document/<int:pk>', login_required(views.DocumentUpdateView.as_view()), name='edit-document'),
    # Supprimer Document
    path('delete-document/<int:pk>', login_required(views.DocumentDeleteView.as_view()), name='delete-document'),

    # Details DataSet
    path('dataset/<int:pk>', login_required(views.DataSetView.as_view()), name='dataset'),
    # Liste DataSet
    path('datasets', login_required(views.DataSetsView.as_view()), name='datasets'),
    # Chercher DataSet
    path('dataset-search', login_required(views.DataSetSearchResultsView.as_view()), name='dataset-search-results'),
    # Creer DataSet
    path('create-dataset', login_required(views.DataSetCreateView.as_view()), name='create-dataset'),
    # Modifier DataSet
    path('edit-dataset/<int:pk>', login_required(views.DataSetUpdateView.as_view()), name='edit-dataset'),
    # Supprimer DataSet
    path('delete-dataset/<int:pk>', login_required(views.DataSetDeleteView.as_view()), name='delete-dataset'),

    # Details Robot
    path('robot/<int:pk>', login_required(views.RobotView.as_view()), name='robot'),
    # Liste Robot
    path('robots', login_required(views.RobotsView.as_view()), name='robots'),
    # Chercher Robot
    path('robot-search', login_required(views.RobotSearchResultsView.as_view()), name='robot-search-results'),
    # Creer Robot
    path('create-robot', login_required(views.RobotCreateView.as_view()), name='create-robot'),
    # Modifier Robot
    path('edit-robot/<int:pk>', login_required(views.RobotUpdateView.as_view()), name='edit-robot'),
    # Supprimer Robot
    path('delete-robot/<int:pk>', login_required(views.RobotDeleteView.as_view()), name='delete-robot'),

]
