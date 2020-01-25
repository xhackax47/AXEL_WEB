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
    #path('new-game/', CreateGameView.as_view(), name='new-game'),
    #path('gameboard/', GameboardView.as_view(), name='gameboard'),
    #path('scores/', ScoresView.as_view(), name='scores'),
    #path('gameover/', GameoverView.as_view(), name='gameover'),
]
