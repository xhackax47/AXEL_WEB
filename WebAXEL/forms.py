from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from WebAXEL.models import Document, DataSet, DocumentCategory, DataSetCategory, AxelUser, RobotCategory, Robot


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AxelUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'profile_img')

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AxelUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]


class DocumentCategoryForm(ModelForm):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ['date_ajout', 'nb_vues']


class DocumentSearchForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class DataSetCategoryForm(ModelForm):
    class Meta:
        model = DataSetCategory
        fields = '__all__'


class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = ['date_ajout']


class DataSetSearchForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = []


class RobotCategoryForm(ModelForm):
    class Meta:
        model = RobotCategory
        fields = '__all__'


class RobotForm(ModelForm):
    class Meta:
        model = Robot
        exclude = ['date_ajout']


class RobotSearchForm(ModelForm):
    class Meta:
        model = Robot
        exclude = []
