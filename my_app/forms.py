from django import forms

from .models import Tema, Razdel


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['text']
        labels = {'text': ''}


class RazdelForm(forms.ModelForm):
    class Meta:
        model = Razdel
        fields = ['text']
        labels = {'text': 'Razdel:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
