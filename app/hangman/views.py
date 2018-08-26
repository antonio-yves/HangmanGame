from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Game(LoginRequiredMixin, TemplateView):
	pass

class Profile(LoginRequiredMixin, TemplateView):
	pass

class AddWord(LoginRequiredMixin, TemplateView):
	pass
