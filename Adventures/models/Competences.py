from django.db.models import Model, IntegerField
from django.utils.translation import ugettext_lazy as _


class Competences(Model):
    Acrobaties = IntegerField(max_length=3, null=False, verbose_name=_("Acrobaties (DEX)"))
    Arcanes = IntegerField(max_length=3, null=False, verbose_name=_("Arcanes (INT)"))
    Athletisme = IntegerField(max_length=3, null=False, verbose_name=_("Athletisme (FOR)"))
    Discretion = IntegerField(max_length=3, null=False, verbose_name=_("Discretion (DEX)"))
    Dressage = IntegerField(max_length=3, null=False, verbose_name=_("Dressage (SAG)"))
    Escamotage = IntegerField(max_length=3, null=False, verbose_name=_("Escamotage (DEX)"))
    Histoire = IntegerField(max_length=3, null=False, verbose_name=_("Histoire (INT)"))
    Intimidation = IntegerField(max_length=3, null=False, verbose_name=_("Intimidation (CHA)"))
    Investigation = IntegerField(max_length=3, null=False, verbose_name=_("Investigation (INT)"))
    Medecine = IntegerField(max_length=3, null=False, verbose_name=_("Medecine (SAG)"))
    Nature = IntegerField(max_length=3, null=False, verbose_name=_("Nature (INT)"))
    Perception = IntegerField(max_length=3, null=False, verbose_name=_("Perception (SAG)"))
    Perspicacite = IntegerField(max_length=3, null=False, verbose_name=_("Perspicacite (SAG)"))
    Persusasion = IntegerField(max_length=3, null=False, verbose_name=_("Persusasion (CHA)"))
    Religion = IntegerField(max_length=3, null=False, verbose_name=_("Religion (INT)"))
    Representation = IntegerField(max_length=3, null=False, verbose_name=_("Representation (CHA)"))
    Survie = IntegerField(max_length=3, null=False, verbose_name=_("Survie (SAG)"))
    Tromperie = IntegerField(max_length=3, null=False, verbose_name=_("Tromperie (CHA)"))
