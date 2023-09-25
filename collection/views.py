from django.shortcuts import render, redirect
from .models import Plyta
from .forms import PlytaForm


def collection(request):
    nosniki = ['CD', 'Vinyl']  # Dostępne opcje nośnika
    selected_nosnik = request.GET.get('nosnik')  # Pobierz wybrany nośnik

    if selected_nosnik:
        plyty = Plyta.objects.filter(nosnik=selected_nosnik)
    else:
        plyty = Plyta.objects.all()

    context = {
        'plyty': plyty,
        'nosniki': nosniki,
        'selected_nosnik': selected_nosnik,
    }

    return render(request, 'collection/collection.html', context)


def dodaj_plyte(request):
    if request.method == 'POST':
        form = PlytaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collection')
    else:
        form = PlytaForm()
    
    context = {'form': form}
    return render(request, 'collection/dodaj_plyte.html', context)
 