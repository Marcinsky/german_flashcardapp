# w flashcardapp/views.py
from django.shortcuts import render, redirect
from .models import NiemieckieSlowo
from .forms import FiszkiForm

def lista_fiszek(request):
    fiszki = NiemieckieSlowo.objects.all()
    return render(request, 'flashcardapp/flashcardapp/lista_fiszek.html', {'fiszki': fiszki})

def dodaj_fiszke(request):
    if request.method == 'POST':
        form = FiszkiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fiszek')
    else:
        form = FiszkiForm()
    return render(request, 'flashcardapp/flashcardapp/dodaj_fiszke.html', {'form': form})
