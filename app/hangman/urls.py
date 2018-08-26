from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as hangman

app_name = 'hangman'

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='core/login.html')),
	path('game/partida/', hangman.Game.as_view(template_name = 'hangman/game/game.html'), name = 'game'),
	path('user/profile/', hangman.Profile.as_view(template_name = 'hangman/user/profile.html'), name = 'profile'),
	path('word/new/', hangman.AddWord.as_view(template_name = 'hangman/user/add-word.html'), name = 'add-word'),
]