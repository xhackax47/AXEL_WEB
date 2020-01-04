from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from WebAXEL.forms import UserCreationForm, UserChangeForm
from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory, AxelUser, AxelGroup


class AxelUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AxelUser
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('date_joined',)


class AxelGroupAdmin(GroupAdmin):
    model = AxelGroup
    can_delete = False


class DocumentCategoryAdmin(ModelAdmin):
    exclude = ['']


class DocumentAdmin(ModelAdmin):
    exclude = ['']
    list_display = (
        'titre', 'date_ajout', 'was_published_recently', 'auteur', 'description', 'document')
    date_hierarchy = 'date_ajout'


class DataSetCategoryAdmin(ModelAdmin):
    exclude = ['']


class DataSetAdmin(ModelAdmin):
    exclude = ['']
    list_display = ('nom', 'date_ajout', 'was_published_recently', 'description', 'dataset')
    date_hierarchy = 'date_ajout'

    def __str__(self):
        return  _("Ensemble de données")


admin.site.unregister(Group)

admin.site.register(AxelUser, AxelUserAdmin)
admin.site.register(AxelGroup, AxelGroupAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
