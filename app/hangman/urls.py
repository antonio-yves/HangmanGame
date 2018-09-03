from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'hangman'

urlpatterns = [
	path('', views.ProfileView.as_view(template_name='hangman/user/profile.html')),
	path('game/partida/<pk>', views.GameView.as_view(), name = 'game'),
	path('user/profile/', views.ProfileView.as_view(template_name = 'hangman/user/profile.html'), name = 'profile'),
	path('word/new/', views.AddWordView.as_view(), name = 'add-word'),
	path('game/new/', views.CreateGameView.as_view(), name = 'create-game'),
]