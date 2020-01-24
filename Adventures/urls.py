from django.urls import path

from Adventures.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('new-character/', CreateCharacterView.as_view(), name='new-character'),
    #path('new-game/', CreateGameView.as_view(), name='new-game'),
    #path('gameboard/', GameboardView.as_view(), name='gameboard'),
    #path('scores/', ScoresView.as_view(), name='scores'),
    #path('gameover/', GameoverView.as_view(), name='gameover'),
]
