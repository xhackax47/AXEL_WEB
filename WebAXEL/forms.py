from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from WebAXEL.models import Document, DataSet, DocumentCategory, DataSetCategory, AxelUser


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = AxelUser
        fields = '__all__'


class UserChangeForm(UserChangeForm):

    class Meta:
        model = AxelUser
        fields = '__all__'


class DocumentCategoryForm(ModelForm):
    class Meta:
        model = DocumentCategory
        exclude = []


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ['date_ajout', 'nb_vues']


class DocumentSearchForm(ModelForm):
    class Meta:
        model = Document
        exclude = []


class DataSetCategoryForm(ModelForm):
    class Meta:
        model = DataSetCategory
        exclude = []


class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = ['date_ajout']


class DataSetSearchForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = []
