import urllib.parse
import urllib.request

from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DeleteView, DetailView
from rest_framework.utils import json
from rest_framework.views import APIView

from AXEL_WEB import settings
from WebAXEL.forms import ConnectForm, SignupForm, UserUpdateForm, DocumentSearchForm, DocumentForm, \
    DataSetSearchForm, DataSetForm, RobotSearchForm, RobotForm
from WebAXEL.multiforms import MultiFormsView
from WebAXEL.models import Document, DataSet, AxelUser, Robot
from WebAXEL.tokens import account_activation_token


class IndexView(MultiFormsView):
    template_name = 'WebAXEL/login/login.html'
    form_classes = {
        'login': ConnectForm,
        'register': SignupForm,
    }
    success_urls = {
        'login': reverse_lazy('login-confirmation'),
        'register': reverse_lazy('register-confirmation'),
    }

    def login_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def register_form_valid(self, form, request):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))


# Vue Login pour la connexion
class ConnectView(LoginView):
    template_name = 'WebAXEL/login/login_confirmation.html'
    redirect_authenticated_user = True
    redirect_field_name = reverse_lazy('index')
    authentication_form = ConnectForm

    def get_success_url(self):
        return reverse_lazy('login-confirmation')


class LoginConfirmationView(TemplateView):
    template_name = 'WebAXEL/login/login_confirmation.html'


# Vue Signup pour l'inscription
class SignupView(CreateView):
    model = AxelUser

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            # Création utilisateur inactif
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # Envoi mail activation
            self.send_activation_mail(request, form, user)
            return redirect('register-confirmation')
        return render(request, 'WebAXEL/registration/register_confirmation.html', {'form': form})

    def send_activation_mail(self, request, form, user):
        # Envoi du mail à l'utilisateur avec le token
        mail_subject = _('Activation du compte A.X.E.L. pour l\'utilisateur {{user.username}}')
        from_email = settings.EMAIL_HOST_USER
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        activation_link = "{0}/activate/{1}/{2}".format(current_site, uid, token)
        html_message = render_to_string('WebAXEL/mail/activation_mail.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': uid,
            'token': token,
            'activation_link': activation_link,
        })
        user.email_user(mail_subject, html_message, from_email)
        messages.success(request, _("Lien d'activation envoyé par mail"))

    def captcha(self, request, user):
        # Captcha
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.load(response)
        if result['success']:
            user.save()
            messages.success(request, _('Utilisateur enregistré avec succès'))
        else:
            messages.error(request, _("Le captcha ne correspond pas"))


class RegisterConfirmationView(TemplateView):
    template_name = 'WebAXEL/registration/register_confirmation.html'


class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        # Décodage base 64 uid et recherche d'utilisateur
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = AxelUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, AxelUser.DoesNotExist):
            user = None
            return messages.warning(request, _("Le lien d'activation est invalide ou ce compte a déjà été activé."))
        if user and account_activation_token.check_token(user, token):
            # Activation de l'utilisateur et enregistrement en BDD
            user.is_active = True
            user.save()
            messages.success(request, _("Votre compte a été activé avec succès"))
            # Connection automatique de l'utilisateur activé
            login(request, user)
            return render(request, 'WebAXEL/mail/active_email.html')
        return render(request, 'WebAXEL/mail/active_email.html')


# Vue Logout pour la deconnexion
class LogoutView(LogoutView):

    # Récupération de la requête de logout
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

    def get_success_url(self):
        return reverse_lazy('index')


# LOGIN REQUIS : Vue AccountSettings pour faire la modification de compte utilisateur à travers un form
class AccountSettingsUsernameView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = AxelUser
    form_class = UserUpdateForm
    template_name = 'WebAXEL/registration/account-settings.html'
    success_url = reverse_lazy('index')

    # Récupération de l'objet via son username
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(AxelUser, username=self.kwargs['username'])

        return user


# LOGIN REQUIS : Vue AccountSettings pour faire la modification de compte utilisateur à travers un form
class AccountSettingsIdView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = AxelUser
    form_class = UserUpdateForm
    template_name = 'WebAXEL/registration/account-settings.html'
    success_url = reverse_lazy('index')

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(AxelUser, pk=self.kwargs['pk'])

        return user


# LOGIN REQUIS : Vue Document qui renvoi les details d'un document
class DocumentView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('index')
    model = Document
    template_name = 'WebAXEL/documents/document.html'


# LOGIN REQUIS : Vue Documents qui renvoi la liste des documents triée et paginée
class DocumentsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = Document
    form_class = DocumentForm
    template_name = 'WebAXEL/documents/create-document.html'
    success_url = reverse_lazy('documents')


# LOGIN REQUIS : Vue DocumentUpdate qui permet la modification d'un document à travers un form
class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = DataSet
    template_name = 'WebAXEL/datasets/dataset.html'


# LOGIN REQUIS : Vue DataSets qui renvoi la liste des datasets triée et paginée
class DataSetsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = DataSet
    form_class = DataSetForm
    template_name = 'WebAXEL/datasets/create-dataset.html'
    success_url = reverse_lazy('datasets')


# LOGIN REQUIS : Vue DataSetUpdate qui permet la modification d'un dataset à travers un form
class DataSetUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = Robot
    template_name = 'WebAXEL/robots/robot.html'


# LOGIN REQUIS : Vue Robots qui renvoi la liste des robots triée et paginée
class RobotsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = Robot
    form_class = RobotForm
    template_name = 'WebAXEL/robots/create-robot.html'
    success_url = reverse_lazy('robots')


# LOGIN REQUIS : Vue RobotUpdate qui permet la modification d'un robot à travers un form
class RobotUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
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
    login_url = reverse_lazy('index')
    model = Robot
    slug_field = 'id'
    success_url = reverse_lazy('robots')
    success_message = "Deleted Successfully"
    template_name = 'WebAXEL/robots/robots_confirmation_modal.html'

    # Récupération de l'objet via son id(pk)
    def get_object(self, *args, **kwargs):
        robot = get_object_or_404(Robot, pk=self.kwargs['pk'])
        return robot
