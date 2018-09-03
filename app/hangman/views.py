from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from random import randint

from django.urls import reverse_lazy

from . import models
from . import forms

class GameView(LoginRequiredMixin, TemplateView):
	pass

class ProfileView(LoginRequiredMixin, TemplateView):
	def get_context_data(self, **kwargs):
		kwargs['partidas'] = models.Game.objects.filter(user = self.request.user)
		print (kwargs)
		return super(ProfileView, self).get_context_data(**kwargs)

class AddWordView(LoginRequiredMixin, CreateView):
	template_name = 'hangman/user/add-word.html'
	model = models.Word
	success_url = reverse_lazy('hangman:profile')
	form_class = forms.AddWordForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		return super(AddWordView, self).form_valid(form)

class CreateGameView(LoginRequiredMixin, View):
	def get(self, request):
		print(self.request.user.pk)
		return redirect('hangman:profile')

	def post(self, request):
		partida = models.Game.objects.filter(user = self.request.user.pk, status = 0)
		if len(partida) == 1:
			return render(request, 'hangman/game/fail.html', {'error': "Não foi possível criar uma nova partida, pois você já possui uma partida em andamento."})
		palavra = models.Word.objects.all()
		if len(palavra) > 1:
			secret_word = randint(1, len(palavra))
			palavra = models.Word.objects.filter(id = secret_word)
			partida = models.Game(user = self.request.user, score = 0, hits = 0, misses = 0, word = palavra)
		elif len(palavra) < 1:
			return render(request, 'hangman/game/fail.html', {'kwargs': "Não foi possível criar uma partida, pois não há palavras cadastradas."})
		else:
			partida = models.Game(user = self.request.user, score = 0, hits = 0, misses = 0, word = palavra[0])
		partida.save()
		partida = models.Game.objects.filter(user = self.request.user.pk, status = 0)
		return redirect('hangman:game', pk = partida[0].pk)

class GameView(LoginRequiredMixin, View):
	def get(self, request, pk):
		partida = models.Game.objects.filter(pk = pk).first()
		secret_word = partida.word.word
		secret_word = secret_word.lower()
		secret_word = list(secret_word)
		letters = list(partida.letters)
		print (secret_word)
		return render(request, 'hangman/game/game.html', {'secret_word': secret_word, 'letras': letters, 'misses': partida.misses})

	def post(self, request, pk):
		partida = models.Game.objects.filter(pk = pk).first()
		secret_word = partida.word.word
		secret_word = secret_word.lower()
		secret_word = list(secret_word)
		letter = request.POST['letter']
		partida.letters += letter
		letters = list(partida.letters)
		if letter in secret_word:
			print ('aqui')
			partida.hits += 1
		else:
			partida.misses += 1
		partida.save()
		if self.verificar(secret_word, letters):
			return render(request, 'hangman/game/fail.html', {'kwargs': "Não foi possível criar uma partida, pois não há palavras cadastradas."})
		return render(request, 'hangman/game/game.html', {'secret_word': secret_word, 'letras': letters, 'misses': partida.misses})

	def verificar(self, secret_word, letters):
		aux = 0
		for letter in secret_word:
			if letter in letters:
				aux += 1
		if aux == len(secret_word):
			return True
		return False


