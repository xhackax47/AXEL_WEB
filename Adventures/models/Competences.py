from django.db.models import Model, IntegerField
from django.utils.translation import ugettext_lazy as _


class Competences(Model):
    Acrobaties = IntegerField(null=False, verbose_name=_("Acrobaties (DEX)"))
    Arcanes = IntegerField(null=False, verbose_name=_("Arcanes (INT)"))
    Athletisme = IntegerField(null=False, verbose_name=_("Athletisme (FOR)"))
    Discretion = IntegerField(null=False, verbose_name=_("Discretion (DEX)"))
    Dressage = IntegerField(null=False, verbose_name=_("Dressage (SAG)"))
    Escamotage = IntegerField(null=False, verbose_name=_("Escamotage (DEX)"))
    Histoire = IntegerField(null=False, verbose_name=_("Histoire (INT)"))
    Intimidation = IntegerField(null=False, verbose_name=_("Intimidation (CHA)"))
    Investigation = IntegerField(null=False, verbose_name=_("Investigation (INT)"))
    Medecine = IntegerField(null=False, verbose_name=_("Medecine (SAG)"))
    Nature = IntegerField(null=False, verbose_name=_("Nature (INT)"))
    Perception = IntegerField(null=False, verbose_name=_("Perception (SAG)"))
    Perspicacite = IntegerField(null=False, verbose_name=_("Perspicacite (SAG)"))
    Persusasion = IntegerField(null=False, verbose_name=_("Persusasion (CHA)"))
    Religion = IntegerField(null=False, verbose_name=_("Religion (INT)"))
    Representation = IntegerField(null=False, verbose_name=_("Representation (CHA)"))
    Survie = IntegerField(null=False, verbose_name=_("Survie (SAG)"))
    Tromperie = IntegerField(null=False, verbose_name=_("Tromperie (CHA)"))
