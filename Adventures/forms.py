from django.forms import ModelForm

# Formulaire de création de personnage
from Adventures.models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = []