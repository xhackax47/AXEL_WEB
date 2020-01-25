from django.forms import ModelForm

# Formulaire de création de personnage
from Adventures.models import Character, Equipment, Competences, Caracteristiques, Physique


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ['equipement', 'competences', 'caracteristiques', 'physique']


class EquipementForm(ModelForm):
    class Meta:
        model = Equipment
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
