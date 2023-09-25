from django.shortcuts import render
from .models import Plyta

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