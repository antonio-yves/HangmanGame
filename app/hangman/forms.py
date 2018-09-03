from django import forms

from . import models

class AddWordForm(forms.ModelForm):
  
  class Meta:
    model = models.Word
    fields = ['user', 'word']
    labels = {
    	'user': 'Usuário',
    	'word': 'Palavra',
    }