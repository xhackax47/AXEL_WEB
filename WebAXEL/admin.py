from django.contrib import admin

from WebAXEL.models import Document, DocumentCategory, DataSet, DataSetCategory


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


admin.site.register(Document, DocumentAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DataSetCategory, DataSetCategoryAdmin)
