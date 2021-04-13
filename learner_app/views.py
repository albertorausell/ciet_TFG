from django.shortcuts import render, HttpResponse
from CiET.variables import Variables

# Create your views here.


def capabilities(request):

    dictionary = {
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'home.html', dictionary)


def evaluations(request):

    return HttpResponse('Evaluations')


def ranking(request):

    return HttpResponse('Ranking')
