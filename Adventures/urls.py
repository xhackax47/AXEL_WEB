from django.contrib.auth.decorators import login_required
from django.urls import path

from Adventures import views
from Adventures.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # Details Personnage
    path('character/<int:pk>', login_required(views.CharacterView.as_view()), name='character'),
    # Liste Personnages
    path('characters/', login_required(views.CharactersView.as_view()), name='characters'),
    # Creer Personnage
    path('new-character/', login_required(views.CharacterCreateView.as_view()), name='new-character'),
    # Ajouter equipement au personnage
    path('new-character/add-equipment/', login_required(views.CharacterEquipmentCreateView.as_view()), name='add-equipment'),
    # Ajouter compétences au personnage
    path('new-character/add-competences/', login_required(views.CharacterCompetencesCreateView.as_view()), name='add-competences'),
    # Ajouter caractéristiques au personnage
    path('new-character/add-carac/', login_required(views.CharacterCaracteristiquesCreateView.as_view()), name='add-carac'),
    # Ajouter physique au personnage
    path('new-character/add-physics/', login_required(views.CharacterPhysiqueCreateView.as_view()), name='add-physics'),
    #path('new-game/', CreateGameView.as_view(), name='new-game'),
    #path('gameboard/', GameboardView.as_view(), name='gameboard'),
    #path('scores/', ScoresView.as_view(), name='scores'),
    #path('gameover/', GameoverView.as_view(), name='gameover'),
]
