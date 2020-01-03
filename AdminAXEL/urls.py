from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('404/', login_required(views.NotFoundView.as_view()), name='404'),
    path('blank/', login_required(views.BlankView.as_view()), name='blank'),
    path('buttons/', login_required(views.ButtonsView.as_view()), name='buttons'),
    path('cards/', login_required(views.CardsView.as_view()), name='cards'),
    path('charts', login_required(views.ChartsView.as_view()), name='charts'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('tables/', login_required(views.TablesView.as_view()), name='tables'),
    path('utilities-animation/', login_required(views.UtilitiesAnimationView.as_view()), name='utilities-animation'),
    path('utilities-border/', login_required(views.UtilitiesBorderView.as_view()), name='utilities-border/'),
    path('utilities-color/', login_required(views.UtilitiesColorView.as_view()), name='utilities-color/'),
    path('utilities-other/', login_required(views.UtilitiesOtherView.as_view()), name='utilities-other/'),
]