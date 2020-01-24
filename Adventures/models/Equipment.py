from django.db.models import Model, IntegerField, ForeignKey
from django.utils.translation import ugettext_lazy as _


class Equipment(Model):
    casque = ForeignKey()
    arme = ForeignKey()
    bouclier = ForeignKey()


class Bourse(Model):
    pieces_platine = IntegerField(max_length=3, blank=True, null=True, default=None,
                                  verbose_name=_("Pièces de platine"))
    pieces_or = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces d'or"))
    pieces_electrum = IntegerField(max_length=3, blank=True, null=True, default=None,
                                   verbose_name=_("Pièces d'électrum"))
    pieces_argent = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces d'argent"))
    pieces_cuivre = IntegerField(max_length=3, blank=True, null=True, default=None, verbose_name=_("Pièces de cuivre"))
