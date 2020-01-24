from django.db.models import Model, IntegerField, FloatField, CharField
from django.utils.translation import ugettext_lazy as _


class Caracteristiques(Model):
    force = IntegerField(max_length=3, null=False, verbose_name=_("Force"))
    dexterite = IntegerField(max_length=3, null=False, verbose_name=_("Points de vie"))
    constitution = IntegerField(max_length=3, null=False, verbose_name=_("Points de vie"))
    intelligence = IntegerField(max_length=3, null=False, verbose_name=_("Points de vie"))
    sagesse = IntegerField(max_length=3, null=False, verbose_name=_("Points de vie"))
    charisme = IntegerField(max_length=3, null=False, verbose_name=_("Points de vie"))


class Physique(Model):
    age = IntegerField(max_length=2, null=False, verbose_name=_("Age"))
    taille = FloatField(max_length=3, null=False, verbose_name=_("Taille"))
    categorie_taille = CharField(max_length=3, null=False, verbose_name=_("Catégorie de taille"))
    poids = IntegerField(max_length=2, null=False, verbose_name=_("Poids"))
    yeux = IntegerField(max_length=2, null=False, verbose_name=_("Yeux"))
    peau = IntegerField(max_length=2, null=False, verbose_name=_("Peau"))
    cheveux = IntegerField(max_length=2, null=False, verbose_name=_("Cheveux"))
