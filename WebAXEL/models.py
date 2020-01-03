from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateTimeField, TextField, FileField, IntegerField, ManyToManyField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Modèles Document
class DocumentCategory(Model):
    categorie = CharField(max_length=255, verbose_name=_("Catégorie du Document"))

    def __str__(self):
        return _("{0}").format(self.categorie)


class Document(Model):
    titre = CharField(max_length=255, verbose_name=_("Titre"))
    date_ajout = DateTimeField(auto_now_add=True,
                               verbose_name=_("Date d'ajout du document"))
    auteur = CharField(max_length=255, null=True, blank=True, verbose_name=_("Auteur du document"))
    description = TextField(null=True, blank=True, verbose_name=_("Description du document"))
    document = FileField(upload_to='static/docs/', null=True, verbose_name=_("Fichier document"))
    nb_vues = IntegerField(default=0, verbose_name=_("Nombre de vues du document"))
    categories_document = ManyToManyField(DocumentCategory, default=None, verbose_name=_("Catégorie du Document"))

    def __str__(self):
        return _("Titre du document : {0}, Date d'ajout du document : {1}, Auteur du document : {2}, "
                 "Description du document : {3}, Emplacement du document : {4}, Catégorie du document : {5}").format(
            self.titre, self.date_ajout,
            self.auteur, self.description,
            self.document, self.categories_document)

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.date_ajout <= now

    was_published_recently.admin_order_field = 'date_ajout'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Publié récemment?')
    was_published_recently.verbose_name = _('Publié récemment?')


# Modèles DataSet
class DataSetCategory(Model):
    categorie = CharField(max_length=255, verbose_name=_("Catégorie de l'ensemble de données"))

    def __str__(self):
        return _("{0}").format(self.categorie)


class DataSet(Model):
    nom = CharField(max_length=255, verbose_name=_("Nom"))
    date_ajout = DateTimeField(auto_now_add=True, verbose_name=_("Date d'ajout de l'ensemble de données"))
    description = TextField(null=True, blank=True, verbose_name=_("Description de l'ensemble de données"))
    dataset = FileField(upload_to='static/datasets/', null=True, verbose_name=_("Fichier ensemble de données"))
    categories_dataset = ManyToManyField(DataSetCategory, default=None,
                                         verbose_name=_("Catégorie de l'ensemble de données"))

    def __str__(self):
        return _(
            "Nom de l'ensemble de données : {0}, Date d'ajout de l'ensemble de données : {1}, "
            "Description de l'ensemble de données : {2}, Emplacement de l'ensemble de données : {3}, "
            "Catégorie de l'ensemble de données : {4}").format(
            self.nom, self.date_ajout,
            self.description, self.dataset,
            self.categories_dataset)

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.date_ajout <= now

    was_published_recently.admin_order_field = 'date_ajout'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Publié récemment?')
    was_published_recently.verbose_name = _('Publié récemment?')
