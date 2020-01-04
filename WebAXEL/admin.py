from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory, AxelUser


class AxelUserInline(admin.StackedInline):
    model = AxelUser
    can_delete = False
    verbose_name = "Utilisateur A.X.E.L."


class AxelUserAdmin(UserAdmin):
    inlines = (AxelUserInline,)


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


admin.site.register(User, AxelUserAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
