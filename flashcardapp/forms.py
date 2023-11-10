# w flashcardapp/forms.py
from django import forms
from .models import NiemieckieSlowo

class FiszkiForm(forms.ModelForm):
    class Meta:
        model = NiemieckieSlowo
        fields = ['slowo_niemieckie', 'slowo_polskie']
