from django.db import models
from django.db.models import Model, IntegerField, ForeignKey, FloatField
from django.utils.translation import ugettext_lazy as _


class Armure(Model):
    prix = IntegerField(max_length=5, blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'armure"))
    ca_bonus = IntegerField(max_length=2, blank=True, null=True, default=None, verbose_name=_("CA Bonus"))
    max_dex = IntegerField(max_length=2, blank=True, null=True, default=None, verbose_name=_("Maximum Dextérité"))
    malus = IntegerField(max_length=2, blank=True, null=True, default=None, verbose_name=_("Malus Armure"))
    echec_sort = IntegerField(max_length=2, blank=True, null=True, default=None,
                              verbose_name=_("Taux en % de chance d'echecs de sort"))
    vitesse_deplacement = FloatField(max_length=2, blank=True, null=True, default=None,
                                     verbose_name=_("Vitesse Déplacement avec armure"))
    poids = IntegerField(max_length=2, blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'armure en livres"))


class Arme(Model):
    prix = IntegerField(max_length=5, blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'arme"))


class Bouclier(Model):
    prix = IntegerField(max_length=5, blank=True, null=True, default=None,
                        verbose_name=_("Prix du bouclier"))


class Bourse(Model):
    pieces_platine = IntegerField(max_length=3, blank=True, null=True, default=None,
                                  verbose_name=_("Pièces de platine"))
    pieces_or = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces d'or"))
    pieces_electrum = IntegerField(max_length=3, blank=True, null=True, default=None,
                                   verbose_name=_("Pièces d'électrum"))
    pieces_argent = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces d'argent"))
    pieces_cuivre = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces de cuivre"))


class Equipment(Model):
    armure = ForeignKey(Armure, on_delete=models.CASCADE)
    arme = ForeignKey(Arme, on_delete=models.CASCADE)
    bouclier = ForeignKey(Bouclier, on_delete=models.CASCADE)
    bourse = ForeignKey(Bourse, on_delete=models.CASCADE)
