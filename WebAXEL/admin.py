from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from WebAXEL.forms import UserCreationForm, UserUpdateForm
from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory, AxelUser, AxelGroup, Robot, \
    RobotCategory


# Gestion des utilisateurs dans l'interface Administrateur de Django
class AxelUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserUpdateForm
    model = AxelUser
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('date_joined',)

    # EN COURS DE DEV
    # actions = ['make_staff']
    #
    # def make_staff(self, request, queryset):
    #     queryset.update(is_staff=True)
    #     self.message_user(request, "Les utilisateurs ont été passés Staff avec succès")
    #
    # make_staff().short_description = "Passer les utilisateurs en Staff"


# Gestion des groupes dans l'interface Administrateur de Django
class AxelGroupAdmin(GroupAdmin):
    model = AxelGroup
    can_delete = False


# Gestion des catégories de document dans l'interface Administrateur de Django
class DocumentCategoryAdmin(ModelAdmin):
    exclude = ['']


# Gestion des catégories de document dans l'interface Administrateur de Django
class DocumentAdmin(ModelAdmin):
    exclude = ['']
    list_display = (
        'titre', 'date_ajout', 'was_published_recently', 'auteur', 'description', 'document')
    date_hierarchy = 'date_ajout'


# Gestion des catégories de dataset dans l'interface Administrateur de Django
class DataSetCategoryAdmin(ModelAdmin):
    exclude = ['']


# Gestion des dataset dans l'interface Administrateur de Django
class DataSetAdmin(ModelAdmin):
    exclude = ['']
    list_display = ('nom', 'date_ajout', 'was_published_recently', 'description', 'dataset')
    date_hierarchy = 'date_ajout'


# Gestion des catégories de robot dans l'interface Administrateur de Django
class RobotCategoryAdmin(ModelAdmin):
    exclude = ['']


# Gestion des robots dans l'interface Administrateur de Django
class RobotAdmin(ModelAdmin):
    exclude = ['']
    list_display = ('nom', 'date_ajout', 'was_published_recently', 'description', 'utilisation', 'doc')
    date_hierarchy = 'date_ajout'

# Desincription des groupes natifs de Django
admin.site.unregister(Group)

# Inscription des modèles dans l'administration
admin.site.register(AxelUser, AxelUserAdmin)
admin.site.register(AxelGroup, AxelGroupAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
admin.site.register(RobotCategory, RobotCategoryAdmin)
