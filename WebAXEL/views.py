import win32com.client
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DeleteView, DetailView

from WebAXEL.forms import DocumentForm, DocumentSearchForm, DataSetForm, DataSetSearchForm, UserChangeForm, \
    RobotSearchForm, RobotForm, UserCreateForm
from WebAXEL.models import Document, DataSet, AxelUser, Robot


# EN COURS DE DEV
# Ouverture des documents Microsoft Word
def get_word(request, *args, **kwargs):
    word = win32com.client.Dispatch('Word.Application')
    return word


# Vue Register pour l'inscription
class RegisterView(CreateView):
    model = AxelUser
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'WebAXEL/registration/register.html'


# Vue Login pour la connexion
class LoginView(LoginView):
    template_name = 'WebAXEL/registration/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


# Vue Logout pour la deconnexion
class LogoutView(TemplateView):
    template_name = 'WebAXEL/registration/login.html'

    # Récupération de la requête de logout
    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)

    def get_success_url(self):
        return reverse_lazy('login')


# LOGIN REQUIS : Vue Index après le login
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'WebAXEL/index.html'


# LOGIN REQUIS : Vue AccountSettings pour faire la modification de compte utilisateur à travers un form
class AccountSettingsView(LoginRequiredMixin, UpdateView):
    model = AxelUser
    form_class = UserChangeForm
    template_name = 'WebAXEL/registration/account-settings.html'
    success_url = reverse_lazy('index')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(AxelUser, username=self.kwargs['username'])

        return user


# LOGIN REQUIS : Vue Document qui renvoi les details d'un document
class DocumentView(LoginRequiredMixin, DetailView):
    model = Document
    template_name = 'WebAXEL/documents/document.html'


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


# LOGIN REQUIS : Vue DocumentDelete qui permet la suppression d'un document en BDD
class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    slug_field = 'id'
    success_url = reverse_lazy('documents')
    success_message = "Deleted Successfully"
    template_name = 'WebAXEL/documents/documents_confirmation_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, queryset=None):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        return document


# LOGIN REQUIS : Vue DataSet qui renvoi les details d'un dataset
class DataSetView(LoginRequiredMixin, DetailView):
    model = DataSet
    template_name = 'WebAXEL/datasets/dataset.html'


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
                Q(nom__icontains=query) | Q(categories_dataset__categorie__icontains=query) | Q(
                    description__icontains=query))
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
    fields = ['nom', 'description', 'source', 'dataset', 'categories_dataset']
    success_url = reverse_lazy('datasets')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        dataset = get_object_or_404(DataSet, pk=self.kwargs['pk'])

        return dataset


# LOGIN REQUIS : Vue DataSetDelete qui permet la suppression d'un dataset en BDD
class DataSetDeleteView(LoginRequiredMixin, DeleteView):
    model = DataSet
    slug_field = 'id'
    success_url = reverse_lazy('datasets')
    success_message = "Deleted Successfully"
    template_name = 'WebAXEL/datasets/datasets_confirmation_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        dataset = get_object_or_404(DataSet, pk=self.kwargs['pk'])
        return dataset


# LOGIN REQUIS : Vue Robot qui renvoi les details d'un robot
class RobotView(LoginRequiredMixin, DetailView):
    model = Robot
    template_name = 'WebAXEL/robots/robot.html'


# LOGIN REQUIS : Vue Robots qui renvoi la liste des robots triée et paginée
class RobotsView(LoginRequiredMixin, ListView):
    model = Robot
    template_name = 'WebAXEL/robots/robots.html'
    queryset = Robot.objects.all()
    context_object_name = 'robots'
    paginate_by = 4

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering


# LOGIN REQUIS : Vue RobotSearchResults qui renvoi la liste des robots triée , paginée et filtrée avec une query
# pour la recherche
class RobotSearchResultsView(LoginRequiredMixin, ListView):
    model = Robot
    form_class = RobotSearchForm
    template_name = 'WebAXEL/robots/robots.html'
    success_url = reverse_lazy('robots')
    paginate_by = 4

    # Requête de filre pour la fonction de recherche
    def get_queryset(self):
        query = self.request.GET.get('search') or None
        # Si il y a une requête on execute le filtre et on renvoi le resultat dans le queryset
        if query:
            queryset = Robot.objects.filter(
                Q(nom__icontains=query) | Q(categories_robot__categorie__icontains=query) | Q(
                    description__icontains=query))
            return queryset
        # Sinon on renvoi une liste de robots vide dans le queryset
        else:
            queryset = Robot.objects.none()
            return queryset

    # Passage des datas du back vers le contexte front
    def get_context_data(self, **kwargs):

        context = super(RobotSearchResultsView, self).get_context_data(**kwargs) or None
        context['robots'] = self.get_queryset()
        return context

    # Tri par date d'ajout
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date_ajout')
        return ordering


# LOGIN REQUIS : Vue RobotCreate qui permet la création d'un robot à travers un form
class RobotCreateView(LoginRequiredMixin, CreateView):
    model = Robot
    form_class = RobotForm
    template_name = 'WebAXEL/robots/create-robot.html'
    success_url = reverse_lazy('robots')


# LOGIN REQUIS : Vue RobotUpdate qui permet la modification d'un robot à travers un form
class RobotUpdateView(LoginRequiredMixin, UpdateView):
    model = Robot
    template_name = 'WebAXEL/robots/edit-robot.html'
    fields = ['nom', 'model', 'utilisation', 'description', 'categories_robot']
    success_url = reverse_lazy('robots')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        robot = get_object_or_404(Robot, pk=self.kwargs['pk'])

        return robot


# LOGIN REQUIS : Vue RobotDelete qui permet la suppression d'un robot en BDD
class RobotDeleteView(LoginRequiredMixin, DeleteView):
    model = Robot
    slug_field = 'id'
    success_url = reverse_lazy('robots')
    success_message = "Deleted Successfully"
    template_name = 'WebAXEL/robots/robots_confirmation_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        robot = get_object_or_404(Robot, pk=self.kwargs['pk'])
        return robot
