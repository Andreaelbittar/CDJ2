from django.shortcuts import render
from .models import Consejos

def home(request):
    consejos = Consejos.objects.all()
    return render(request, 'home.html', {'consejos': consejos})

def consejos_locales_curul(request):
    consejos = Consejos.objects.filter(type_consejo='Curul')
    return render(request, 'consejos_locales.html', {'consejos': consejos})


def consejos_locales(request):
    consejos = Consejos.objects.filter(type_consejo='Local')
    context = {'consejos': consejos}
    return render(request, 'consejos_locales.html', context)