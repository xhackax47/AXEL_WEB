from django.db import models
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, FloatField
from django.utils.translation import ugettext_lazy as _

from Adventures.models import Caracteristiques, Competences, Equipment
from Adventures.models.Caracteristiques import Physique


class Character(Model):
    nom = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom"))
    alignement = CharField(max_length=100, unique=True, null=True, verbose_name=_("Alignement"))
    race = CharField(max_length=100, null=False, verbose_name=_("Race"))
    classe = CharField(max_length=100, null=False, verbose_name=_("Classe"))
    pv_actuels = IntegerField(null=False, verbose_name=_("Points de vie à l'instanté"))
    pv_temporaires = IntegerField(null=False, verbose_name=_("Points de vie temporaires"))
    level = IntegerField(null=False, verbose_name=_("Niveau"))
    xp = IntegerField(blank=True, default=None, verbose_name=_("Experience"))

    bonus_maitrise = IntegerField(default=None, verbose_name=_("Bonus de maitrîse"))
    ca = IntegerField(default=None, verbose_name=_("Classe d'armure"))
    initiative = IntegerField(default=None, verbose_name=_("Initiative"))
    vitesse_deplacement = FloatField(max_length=2, default=None, verbose_name=_("Vitesse de déplacement"))

    equipement = ForeignKey(Equipment, on_delete=models.CASCADE, default=None)
    competences = ForeignKey(Competences, on_delete=models.CASCADE, default=None)
    caracteristiques = ForeignKey(Caracteristiques, on_delete=models.CASCADE, default=None)
    physique = ForeignKey(Physique, on_delete=models.CASCADE, default=None)


class NPCFonction(TextChoices):
    Marchand = _('Marchand')
    Quete = _('Quête')
    Discussion = _('Discussion')


class NPC(Model):
    nom = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom"))
    race = CharField(max_length=100, null=False, verbose_name=_("Race"))
    classe = CharField(max_length=100, null=False, verbose_name=_("Classe"))
    pv = IntegerField(null=False, verbose_name=_("Points de vie"))
    level = IntegerField(null=False, verbose_name=_("Niveau"))
    ca = IntegerField(default=None, verbose_name=_("Classe d'armure"))
    vitesse_deplacement = FloatField(max_length=2, default=None, verbose_name=_("Vitesse de déplacement"))

    equipement = ForeignKey(Equipment, on_delete=models.CASCADE, default=None)
    competences = ForeignKey(Competences, on_delete=models.CASCADE, default=None)
    caracteristiques = ForeignKey(Caracteristiques, on_delete=models.CASCADE, default=None)
    physique = ForeignKey(Physique, on_delete=models.CASCADE, default=None)

    fonction = CharField(max_length=100, choices=NPCFonction.choices, default=NPCFonction.Discussion,
                         verbose_name=_("Fonction du PNJ"))
