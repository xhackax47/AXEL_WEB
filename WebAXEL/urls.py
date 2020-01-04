from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

urlpatterns = [
    # Authentication
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Internationalisation
    path('i18n/', include('django.conf.urls.i18n')),
    # Index
    path('', login_required(views.IndexView.as_view()), name='index'),
    # Gestion de compte
    path('account-settings/<int:pk>', login_required(views.AccountSettingsView.as_view()), name='account-settings'),

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