from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path, include

from . import views


# app_name = 'WebAXEL'

def test_trigger_error(request):
    division_by_zero = 1 / 0


# Base
urlpatterns = [
    # Accueil
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    # Internationalisation
    path('i18n/', include('django.conf.urls.i18n')),
    # Test case pour Sentry
    path('sentry-debug/', test_trigger_error, name='sentry-debug'),
]
# Comptes et connexion
urlpatterns += [
    # Inscription
    path('register/', views.SignupView.as_view(), name='register'),
    path('register-confirmation/', views.RegisterConfirmationView.as_view(), name='register-confirmation'),
    # Authentification
    path('login/', views.LoginView.as_view(), name='login'),
    path('login-confirmation/', views.LoginConfirmationView.as_view(), name='login-confirmation'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Gestion de compte par username
    url(r'^account-settings-username/(?P<username>\w+)/$', login_required(views.AccountSettingsUsernameView.as_view()),
        name='account-settings-username'),
    # Gestion compte par id
    path('account-settings-id/<int:pk>', views.AccountSettingsIdView.as_view(), name='account-settings-id'),
    # Activation mail des comptes
    path('activate/<str:uidb64>/<str:token>', views.ActivateAccount.as_view(), name='activate'),
]
# Documents
urlpatterns += [
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
]
# Datasets
urlpatterns += [
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
]
# Robots
urlpatterns += [
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
