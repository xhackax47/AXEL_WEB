from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from WebAXEL.forms import UserCreationForm, UserChangeForm
from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory, AxelUser


class AxelUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AxelUser
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'username',  'is_staff', 'is_active',)
    verbose_name = "Utilisateur A.X.E.L."
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('date_joined',)


class DocumentCategoryAdmin(admin.ModelAdmin):
    exclude = ['']


class DocumentAdmin(admin.ModelAdmin):
    exclude = ['']
    list_display = (
        'titre', 'date_ajout', 'was_published_recently', 'auteur', 'description', 'document')
    date_hierarchy = 'date_ajout'


class DataSetCategoryAdmin(admin.ModelAdmin):
    exclude = ['']


class DataSetAdmin(admin.ModelAdmin):
    exclude = ['']
    list_display = ('nom', 'date_ajout', 'was_published_recently', 'description', 'dataset')
    date_hierarchy = 'date_ajout'


admin.site.register(AxelUser, AxelUserAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
