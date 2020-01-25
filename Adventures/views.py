from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from Adventures.forms import CharacterForm
from Adventures.models import Character


class IndexView(TemplateView):
    template_name = "Adventures/index.html"


# LOGIN REQUIS : Vue Character qui renvoi les details d'un personnage
class CharacterView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = 'Adventures/characters/character.html'


# LOGIN REQUIS : Vue Characters qui renvoi la liste des personnages
class CharactersView(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'Adventures/characters/characters.html'
    queryset = Character.objects.all()
    context_object_name = 'characters'
    paginate_by = 4


# LOGIN REQUIS : Vue CharacterCreate qui permet la création d'un personnage à travers un form
class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'Adventures/characters/create-character.html'
    success_url = reverse_lazy('character')
