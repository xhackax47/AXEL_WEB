from django.contrib.auth.models import User
from django.forms import ModelForm

from WebAXEL.models import Document, DataSet, DocumentCategory, DataSetCategory


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['password']


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
