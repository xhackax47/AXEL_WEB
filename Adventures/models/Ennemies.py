from django.db import models
from django.db.models import TextChoices, Model, CharField, IntegerField, FloatField, ForeignKey
from django.utils.translation import ugettext_lazy as _


from Adventures.models import Competences, Caracteristiques
from Adventures.models.Equipment import Equipement


class EnnemyFonction(TextChoices):
    Sbire = _('Sbire')
    Capitaine = _('Capitaine')
    Boss = _('Boss')


class Ennemy(Model):
    nom = CharField(max_length=100, unique=True, null=True, verbose_name=_("Nom"))
    race = CharField(max_length=100, null=False, verbose_name=_("Race"))
    classe = CharField(max_length=100, null=False, verbose_name=_("Classe"))
    pv = IntegerField(null=False, verbose_name=_("Points de vie"))
    level = IntegerField(null=False, verbose_name=_("Niveau"))
    ca = IntegerField(default=None, verbose_name=_("Classe d'armure"))
    vitesse_deplacement = FloatField(max_length=2, default=None, verbose_name=_("Vitesse de déplacement"))

    equipement = ForeignKey(Equipement, on_delete=models.CASCADE)
    competences = ForeignKey(Competences, on_delete=models.CASCADE)
    caracteristiques = ForeignKey(Caracteristiques, on_delete=models.CASCADE)

    fonction = CharField(max_length=100, choices=EnnemyFonction.choices, default=EnnemyFonction.Sbire,
                         verbose_name=_("Fonction de l'ennemi"))

    def __str__(self):
        return self.nom
