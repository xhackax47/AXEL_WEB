from django.db import models
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, FloatField
from django.utils.translation import ugettext_lazy as _

from Adventures.models import Caracteristiques, Competences, Equipment
from Adventures.models.Caracteristiques import Physique


class Character(Model):
    name = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom"))
    alignement = CharField(max_length=100, unique=True, null=True, verbose_name=_("Alignement"))
    race = CharField(max_length=100, null=False, verbose_name=_("Race"))
    classe = CharField(max_length=100, null=False, verbose_name=_("Classe"))
    pv_actuels = IntegerField(max_length=4, null=False, verbose_name=_("Points de vie à l'instanté"))
    pv_temporaires = IntegerField(max_length=4, null=False, verbose_name=_("Points de vie temporaires"))
    level = IntegerField(max_length=3, null=False, verbose_name=_("Niveau"))
    xp = IntegerField(max_length=5, blank=True, default=None, verbose_name=_("Experience"))

    bonus_maitrise = IntegerField(max_length=3, default=None, verbose_name=_("Bonus de maitrîse"))
    ca = IntegerField(max_length=3, default=None, verbose_name=_("Classe d'armure"))
    initiative = IntegerField(max_length=3, default=None, verbose_name=_("Initiative"))
    vitesse_deplacement = FloatField(max_length=2, default=None, verbose_name=_("Vitesse de déplacement"))

    equipement = ForeignKey(Equipment, on_delete=models.CASCADE)
    competences = ForeignKey(Competences, on_delete=models.CASCADE)
    caracteristiques = ForeignKey(Caracteristiques, on_delete=models.CASCADE)
    physique = ForeignKey(Physique, on_delete=models.CASCADE)


class NPCFonction(TextChoices):
    Marchand = _('Marchand')
    Quete = _('Quête')
    Discussion = _('Discussion')


class NPC(Model):
    name = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom"))
    race = CharField(max_length=100, null=False, verbose_name=_("Race"))
    classe = CharField(max_length=100, null=False, verbose_name=_("Classe"))
    pv = IntegerField(max_length=4, null=False, verbose_name=_("Points de vie"))
    level = IntegerField(max_length=3, null=False, verbose_name=_("Niveau"))
    ca = IntegerField(max_length=3, default=None, verbose_name=_("Classe d'armure"))
    vitesse_deplacement = FloatField(max_length=2, default=None, verbose_name=_("Vitesse de déplacement"))

    equipement = ForeignKey(Equipment, on_delete=models.CASCADE)
    competences = ForeignKey(Competences, on_delete=models.CASCADE)
    caracteristiques = ForeignKey(Caracteristiques, on_delete=models.CASCADE)

    fonction = CharField(max_length=100, choices=NPCFonction.choices, default=NPCFonction.Discussion,
                         verbose_name=_("Fonction du PNJ"))
