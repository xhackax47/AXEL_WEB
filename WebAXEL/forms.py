from django.forms import ModelForm, CharField, PasswordInput

from WebAXEL.models import Document, DataSet, DocumentCategory, DataSetCategory, AxelUser


class UserForm(ModelForm):
    class Meta:
        model = AxelUser
        exclude = ['user']


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
