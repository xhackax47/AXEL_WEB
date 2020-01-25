from django.db import models
from django.db.models import Model, IntegerField, ForeignKey, FloatField, CharField, BooleanField
from django.utils.translation import ugettext_lazy as _


class Armure(Model):
    TYPE_ARMURE = (
        ('1', _('Armure légère')),
        ('2', _('Armure intermédiaire')),
        ('3', _('Armure lourde')),
    )
    nom = CharField(max_length=100, verbose_name="Nom de l'armure", default=None)
    prix = IntegerField(blank=True, null=True, default=None, verbose_name=_("Prix de l'armure"))
    type_armure = CharField(max_length=100, choices=TYPE_ARMURE, verbose_name="Type de l'armure", default=None)
    ca_bonus = IntegerField(blank=True, null=True, default=None, verbose_name=_("CA Bonus"))
    max_dex = IntegerField(blank=True, null=True, default=None, verbose_name=_("Maximum Dextérité"))
    malus = IntegerField(blank=True, null=True, default=None, verbose_name=_("Malus Armure"))
    echec_sort = IntegerField(blank=True, null=True, default=None,
                              verbose_name=_("Taux en % de chance d'echecs de sort"))
    vitesse_deplacement = FloatField(max_length=2, blank=True, null=True, default=None,
                                     verbose_name=_("Vitesse Déplacement avec armure"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'armure en livres"))
    discretion = BooleanField(blank=True, null=True, default=None, verbose_name=_("Armure discrète ?"))

    def __str__(self):
        return self.nom


class Arme(Model):
    class Type_Arme(models.TextChoices):
        courantes_cac = _('Armes courantes de corps à corps'),
        courantes_dist = _('Armes courantes à distance'),
        guerre_cac = _('Armes de guerre de corps à corps'),
        guerre_dist = _('Armes de guerre à distance')

    class Type_Degats(models.TextChoices):
        cont = '1', _('Contondant'),
        perf = '2', _('Perforant'),
        tran = '3', _('Tranchant')

    nom = CharField(max_length=100, verbose_name="Nom de l'arme", default=None)
    prix = IntegerField(blank=True, null=True, default=None, verbose_name=_("Prix de l'arme"))
    type_arme = CharField(max_length=100, choices=Type_Arme.choices, verbose_name="Type de l'arme", default=Type_Arme.courantes_cac)
    type_degats = CharField(max_length=100, choices=Type_Degats.choices, verbose_name="Type de dégâts de l'arme", default=Type_Degats.cont)

    degat = IntegerField(null=False, blank=False, default=1)
    poids = IntegerField(blank=True, null=True, default=None, verbose_name=_("Poids de l'arme en kilogrammes"))
    proprietes = CharField(max_length=255, blank=True, null=True, default=None, verbose_name=_("Propriétés de l'arme"))

    def __str__(self):
        return self.nom


class Bourse(Model):
    pieces_platine = IntegerField(blank=True, null=True, default=None,
                                  verbose_name=_("Pièces de platine"))
    pieces_or = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces d'or"))
    pieces_electrum = IntegerField(blank=True, null=True, default=None,
                                   verbose_name=_("Pièces d'électrum"))
    pieces_argent = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces d'argent"))
    pieces_cuivre = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces de cuivre"))

    def __str__(self):
        return _(
            "Nombre de pièces de platine : {0}, "
            "Nombre de pièces d'or : {1}, "
            "Nombre de pièces d'électrum : {2}, "
            "Nombre de pièces d'argent : {3}, "
            "Nombre de pièces de cuivre : {4}, ").format(
            self.pieces_platine, self.pieces_or, self.pieces_electrum, self.pieces_argent, self.pieces_cuivre
        )


class Objet(Model):
    nom = CharField(max_length=255, verbose_name="Nom de l'objet", null=True, default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'objet"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'objet"))

    def __str__(self):
        return self.nom


class Outil(Model):
    nom = CharField(max_length=255, verbose_name="Nom de l'outil", null=True, default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'outil"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'outil"))

    def __str__(self):
        return self.nom


class Equipement(Model):
    armure = ForeignKey(Armure, on_delete=models.CASCADE, default=None)
    armes = ForeignKey(Arme, on_delete=models.CASCADE, default=None)
    bourse = ForeignKey(Bourse, on_delete=models.CASCADE, default=None)
    objets = ForeignKey(Objet, on_delete=models.CASCADE, default=None)
    outils = ForeignKey(Outil, on_delete=models.CASCADE, default=None)
