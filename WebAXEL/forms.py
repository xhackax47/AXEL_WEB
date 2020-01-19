from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, CharField, HiddenInput, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from WebAXEL.models import Document, DataSet, DocumentCategory, DataSetCategory, AxelUser, RobotCategory, Robot


class MultipleForm(forms.Form):
    action = CharField(max_length=60, widget=HiddenInput())


# Formulaire de connexion utilisateur
class AuthenticationForm(AuthenticationForm, MultipleForm):
    class Meta(AuthenticationForm):
        model = AxelUser


# Formulaire d'inscription utilisateur
class SignupForm(UserCreationForm, MultipleForm):
    email = EmailField(max_length=200, help_text=_('Obligatoire'))

    class Meta(UserCreationForm):
        model = AxelUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = AxelUser.objects.filter(username=username)
        if r.count():
            error = _('Username already exists.')
            raise ValidationError(error)
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = AxelUser.objects.filter(email=email)
        if r.count():
            error = _('Email already exists')
            raise ValidationError(error)
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            error = _('Passwords don\'t match')
            raise ValidationError(error)
        return password2


# Formulaire de modification des informations utilisateur
class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['date_joined'].widget.attrs['readonly'] = True
        self.fields['last_login'].widget.attrs['readonly'] = True

    class Meta:
        model = AxelUser
        exclude = ['is_superuser', 'is_staff', 'user_permissions', 'groups', 'password']


# Formulaire d'ajout de catégorie de Document
class DocumentCategoryForm(ModelForm):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


# Formulaire d'ajout de Document
class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ['date_ajout', 'nb_vues']


# Formulaire de recherche de Document
class DocumentSearchForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


# Formulaire d'ajout de catégorie de Dataset
class DataSetCategoryForm(ModelForm):
    class Meta:
        model = DataSetCategory
        fields = '__all__'


# Formulaire d'ajout de Dataset
class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = ['date_ajout', 'nb_vues']


# Formulaire de recherche de Dataset
class DataSetSearchForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = []


# Formulaire d'ajout de catégorie de Robot
class RobotCategoryForm(ModelForm):
    class Meta:
        model = RobotCategory
        fields = '__all__'


# Formulaire d'ajout de Robot
class RobotForm(ModelForm):
    class Meta:
        model = Robot
        exclude = ['date_ajout', 'nb_vues']


# Formulaire de recherche de Robot
class RobotSearchForm(ModelForm):
    class Meta:
        model = Robot
        exclude = []
