from django.forms import ModelForm

# Formulaire de création de personnage
from Adventures.models import Character, Competences, Caracteristiques, Physique, Equipement


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ['equipement', 'competences', 'caracteristiques', 'physique', 'user']


class EquipementForm(ModelForm):
    class Meta:
        model = Equipement
        exclude = []


class CompetencesForm(ModelForm):
    class Meta:
        model = Competences
        exclude = []


class CaracteristiquesForm(ModelForm):
    class Meta:
        model = Caracteristiques
        exclude = []


class PhysiqueForm(ModelForm):
    class Meta:
        model = Physique
        exclude = []
