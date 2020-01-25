from django.db.models import Model, IntegerField, FloatField, CharField
from django.utils.translation import ugettext_lazy as _


class Caracteristiques(Model):
    force = IntegerField(null=False, verbose_name=_("Force"))
    dexterite = IntegerField(null=False, verbose_name=_("Dexterité"))
    constitution = IntegerField(null=False, verbose_name=_("Constitution"))
    intelligence = IntegerField(null=False, verbose_name=_("Intelligence"))
    sagesse = IntegerField(null=False, verbose_name=_("Sagesse"))
    charisme = IntegerField(null=False, verbose_name=_("Charisme"))


class Physique(Model):
    age = IntegerField(null=False, verbose_name=_("Age"))
    taille = FloatField(null=False, verbose_name=_("Taille"))
    categorie_taille = CharField(max_length=2, null=False, default=None, verbose_name=_("Catégorie de taille"))
    poids = IntegerField(null=False, verbose_name=_("Poids"))
    yeux = IntegerField(null=False, verbose_name=_("Yeux"))
    peau = IntegerField(null=False, verbose_name=_("Peau"))
    cheveux = IntegerField(null=False, verbose_name=_("Cheveux"))
