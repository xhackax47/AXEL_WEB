import win32com.client
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DeleteView

from WebAXEL.forms import UserForm, DocumentForm, DocumentSearchForm, DataSetForm, DataSetSearchForm
from WebAXEL.models import Document, DataSet


# Vue Login pour la connexion
class LoginView(TemplateView):
    template_name = 'registration/login.html'

    # Methode POST de la vue Login
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


# Vue Logout pour la deconnexion
class LogoutView(TemplateView):
    template_name = 'WebAXEL/index.html'

    # Récupération de la requête de logout
    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)


# LOGIN REQUIS : Vue Index après le login
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'WebAXEL/index.html'


# LOGIN REQUIS : Vue AccountSettings pour faire la modification de compte utilisateur à travers un form
class AccountSettingsView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'registration/account-settings.html'
    success_url = reverse_lazy('index')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])

        return user


# LOGIN REQUIS : Vue Documents qui renvoi la liste des documents triée et paginée
class DocumentsView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'WebAXEL/documents/documents.html'
    queryset = Document.objects.all()
    context_object_name = 'documents'
    paginate_by = 4

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering

    # EN COURS DE DEV
    # Ouverture des documents Microsoft Word
    def get_word(self, request, *args, **kwargs):
        word = win32com.client.Dispatch('Word.Application')
        return word


# LOGIN REQUIS : Vue DocumentSearchResults qui renvoi la liste des documents triée, paginée et filtrée avec une query
# pour la recherche
class DocumentSearchResultsView(LoginRequiredMixin, ListView):
    model = Document
    form_class = DocumentSearchForm
    template_name = 'WebAXEL/documents/documents.html'
    success_url = reverse_lazy('documents')
    paginate_by = 4

    # Requête de filre pour la fonction de recherche
    def get_queryset(self):
        query = self.request.GET.get('search') or None
        # Si il y a une requête on execute le filtre et on renvoi le resultat dans le queryset
        if query:
            queryset = Document.objects.filter(
                Q(titre__icontains=query) | Q(auteur__icontains=query) | Q(description__icontains=query))
            return queryset
        # Sinon on renvoi une liste de document vide dans le queryset
        else:
            queryset = Document.objects.none()
            return queryset

    # Passage des datas du back vers le contexte front
    def get_context_data(self, **kwargs):

        context = super(DocumentSearchResultsView, self).get_context_data(**kwargs) or None
        context['documents'] = self.get_queryset()
        return context

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering


# LOGIN REQUIS : Vue DocumentCreate qui permet la création d'un document à travers un form
class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'WebAXEL/documents/create-document.html'
    success_url = reverse_lazy('documents')


# LOGIN REQUIS : Vue DocumentUpdate qui permet la modification d'un document à travers un form
class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    template_name = 'WebAXEL/documents/edit-document.html'
    fields = ['titre', 'auteur', 'description', 'document', 'categories_document']
    success_url = reverse_lazy('documents')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])

        return document


# LOGIN REQUIS : Vue DocumentDelete qui permet la suppression d'un document
class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    success_url = reverse_lazy('documents')
    template_name = 'WebAXEL/documents/confirm_delete_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        return document


# LOGIN REQUIS : Vue DataSets qui renvoi la liste des datasets triée et paginée
class DataSetsView(LoginRequiredMixin, ListView):
    model = DataSet
    template_name = 'WebAXEL/datasets/datasets.html'
    queryset = DataSet.objects.all()
    context_object_name = 'datasets'
    paginate_by = 4

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering


# LOGIN REQUIS : Vue DataSetSearchResults qui renvoi la liste des datasets triée , paginée et filtrée avec une query
# pour la recherche
class DataSetSearchResultsView(LoginRequiredMixin, ListView):
    model = DataSet
    form_class = DataSetSearchForm
    template_name = 'WebAXEL/datasets/datasets.html'
    success_url = reverse_lazy('datasets')
    paginate_by = 4

    # Requête de filre pour la fonction de recherche
    def get_queryset(self):
        query = self.request.GET.get('search') or None
        # Si il y a une requête on execute le filtre et on renvoi le resultat dans le queryset
        if query:
            queryset = DataSet.objects.filter(
                Q(nom__icontains=query) | Q(categories_dataset__categorie__icontains=query) | Q(description__icontains=query))
            return queryset
        # Sinon on renvoi une liste de datasets vide dans le queryset
        else:
            queryset = DataSet.objects.none()
            return queryset

    # Passage des datas du back vers le contexte front
    def get_context_data(self, **kwargs):

        context = super(DataSetSearchResultsView, self).get_context_data(**kwargs) or None
        context['datasets'] = self.get_queryset()
        return context

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering


# LOGIN REQUIS : Vue DataSetCreate qui permet la création d'un dataset à travers un form
class DataSetCreateView(LoginRequiredMixin, CreateView):
    model = DataSet
    form_class = DataSetForm
    template_name = 'WebAXEL/datasets/create-dataset.html'
    success_url = reverse_lazy('datasets')


# LOGIN REQUIS : Vue DataSetUpdate qui permet la modification d'un dataset à travers un form
class DataSetUpdateView(LoginRequiredMixin, UpdateView):
    model = DataSet
    template_name = 'WebAXEL/datasets/edit-dataset.html'
    fields = ['nom', 'description', 'dataset', 'categories-datasets']
    success_url = reverse_lazy('datasets')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        dataset = get_object_or_404(DataSet, pk=self.kwargs['pk'])

        return dataset


# LOGIN REQUIS : Vue DataSetDelete qui permet la suppression d'un dataset
class DataSetDeleteView(LoginRequiredMixin, DeleteView):
    model = DataSet
    success_url = reverse_lazy('datasets')
    template_name = 'WebAXEL/datasets/confirm_delete_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        dataset = get_object_or_404(DataSet, pk=self.kwargs['pk'])
        return dataset
