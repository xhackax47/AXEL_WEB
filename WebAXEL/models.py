from datetime import timedelta

from django.contrib.auth.models import AbstractUser, Group, User
from django.db.models import Model, CharField, DateTimeField, TextField, FileField, IntegerField, ManyToManyField, \
    ImageField, EmailField, TextChoices, URLField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


# Modèle Groupe personnalisé (Extension du groupe de base de Django)
class AxelGroup(Group):
    description = CharField(max_length=1024)

    def __str__(self):
        return "Groupe A.X.E.L."


# Modèle User personnalisé (Extension de l'utlisateur de base de Django)
class AxelUser(AbstractUser):
    # Classe interne de fonctions informatif (Aucun changement de permissions)
    class Fonction(TextChoices):
        Guest = _('Visiteur')
        User = _('Utilisateur')
        Dev = _('Développeur')
        DjangAdmin = _('Administrateur Django')
        AxelAdmin = _('Administrateur A.X.E.L.')
        SuperAdmin = _('Super Administrateur')

    username = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom d'utilisateur"))
    email = EmailField(_('email address'), unique=True)
    profile_img = ImageField(upload_to='static/img/profilesImages/', blank=True, verbose_name=_("Image Profil"))
    fonction = CharField(max_length=100, choices=Fonction.choices, default=Fonction.Guest, verbose_name=_("Fonction"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return _("Nom d'utilisateur {0} / Adresse email : {1} ").format(self.username, self.email)


# DOCUMENTS

# Modèle Catégorie de document
class DocumentCategory(Model):
    categorie = CharField(max_length=255, verbose_name=_("Catégorie du Document"))

    def __str__(self):
        return self.categorie.__str__()


# Modèle Document
class Document(Model):
    titre = CharField(max_length=255, verbose_name=_("Titre"))
    date_ajout = DateTimeField(auto_now_add=True,
                               verbose_name=_("Date d'ajout du document"))
    auteur = CharField(max_length=255, null=True, blank=True, verbose_name=_("Auteur du document"))
    description = TextField(null=True, blank=True, verbose_name=_("Description du document"))
    document = FileField(upload_to='static/docs/', null=True, verbose_name=_("Fichier document"))
    nb_vues = IntegerField(default=0, verbose_name=_("Nombre de vues du document"))
    categories_document = ManyToManyField(DocumentCategory, blank=True, default=None,
                                          verbose_name=_("Catégories du Document"))

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


# DATASETS

# Modèle Catégorie de dataset
class DataSetCategory(Model):
    categorie = CharField(max_length=255, verbose_name=_("Catégorie du jeu de données"))

    def __str__(self):
        return self.categorie.__str__()


# Modèles DataSet
class DataSet(Model):
    nom = CharField(max_length=255, verbose_name=_("Nom"))
    date_ajout = DateTimeField(auto_now_add=True, verbose_name=_("Date d'ajout du jeu de données"))
    description = TextField(null=True, blank=True, verbose_name=_("Description du jeu de données"))
    dataset = FileField(upload_to='static/datasets/', null=True, verbose_name=_("Fichier jeu de données"))
    source = URLField(max_length=1000, verbose_name=_("Source"), blank=True)
    nb_vues = IntegerField(default=0, verbose_name=_("Nombre de vues du jeu de données"))
    categories_dataset = ManyToManyField(DataSetCategory, blank=True, default=None,
                                         verbose_name=_("Catégories du jeu de données"))

    def __str__(self):
        return _(
            "Nom du jeu de données : {0}, Date d'ajout du jeu de données : {1}, "
            "Description du jeu de données : {2}, Emplacement du jeu de données : {3}, "
            "Catégories du jeu de données : {4}").format(
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


# ROBOTS

# Modèle Catégorie de robot
class RobotCategory(Model):
    categorie = CharField(max_length=255, verbose_name=_("Catégorie du robot"))

    def __str__(self):
        return self.categorie.__str__()


# Modèle Robot
class Robot(Model):
    nom = CharField(max_length=255, verbose_name=_("Nom"))
    image = ImageField(upload_to='static/img/robots', blank=True, verbose_name=_("Image Robot"))
    model = CharField(max_length=255, verbose_name=_("Modèle"))
    utilisation = CharField(max_length=1000, verbose_name=_("Utilisation"))
    doc = FileField(upload_to='static/robots/', null=True, verbose_name=_("Documentation Robot"))
    date_ajout = DateTimeField(auto_now_add=True, verbose_name=_("Date d'ajout du robot"))
    description = TextField(null=True, blank=True, verbose_name=_("Description du robot"))
    nb_vues = IntegerField(default=0, verbose_name=_("Nombre de vues du robot"))
    categories_robot = ManyToManyField(RobotCategory, blank=True, default=None,
                                       verbose_name=_("Catégories du robot"))

    def __str__(self):
        return _(
            "Nom du robot : {0}, Date d'ajout du robot: {1}, "
            "Description du robot : {2}, Catégories du robot: {3}, ".format(
                self.nom, self.date_ajout,
                self.description, self.categories_robot))

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.date_ajout <= now

    was_published_recently.admin_order_field = 'date_ajout'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Publié récemment?')
    was_published_recently.verbose_name = _('Publié récemment?')
