from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from WebAXEL.forms import UserCreationForm, UserUpdateForm
from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory, AxelUser, AxelGroup, Robot, \
    RobotCategory


class AxelUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserUpdateForm
    model = AxelUser
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'is_active',)
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('date_joined',)
    actions = ['make_staff']

    def make_staff(self, request, queryset):
        queryset.update(is_staff=True)
    make_staff().short_description = "Passer les utilisateurs en Staff"


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


class RobotCategoryAdmin(ModelAdmin):
    exclude = ['']


class RobotAdmin(ModelAdmin):
    exclude = ['']
    list_display = ('nom', 'date_ajout', 'was_published_recently', 'description', 'utilisation', 'doc')
    date_hierarchy = 'date_ajout'


admin.site.unregister(Group)

admin.site.register(AxelUser, AxelUserAdmin)
admin.site.register(AxelGroup, AxelGroupAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
admin.site.register(RobotCategory, RobotCategoryAdmin)
