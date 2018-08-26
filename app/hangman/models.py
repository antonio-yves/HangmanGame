from django.db import models
from app.core.models import UUIDUser

class Word(models.Model):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'Usuário')
	word = models.CharField(max_length = 255, verbose_name = 'Palavra')

	def __str__(self):
		return self.word

	class Meta:
		verbose_name = 'Palavra'
		verbose_name_plural = 'Palavras'

class Game(models.Model):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'Usuário')
	word = models.ForeignKey(Word, on_delete = models.CASCADE, related_name = 'words', verbose_name = 'Palavra')
	status = models.IntegerField(verbose_name = 'Status', default = 0)
	score = models.IntegerField(verbose_name = 'Pontos')

	def __str__(self):
		return 'Partida %i | %s' % (self.pk, self.user.first_name)

	class Meta:
		verbose_name = 'Partida'
		verbose_name_plural = 'Partidas'

class Score(models.Model):
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'use', verbose_name = 'Usuário')
	score = models.IntegerField(verbose_name = 'Pontuação')

	def __str__(self):
		return 'Pontuação do Usuário: %s | %i pontos' % (self.user.first_name, self.score)

	class Meta:
		verbose_name = 'Pontuação'
		verbose_name_plural = 'Pontuações'