from django.shortcuts import render, HttpResponse
from CiET.variables import Variables

# Create your views here.


def capabilities(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'learner_app/templates/capabilities.html', dictionary)


def evaluations(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'evaluations.html', dictionary)


def ranking(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'ranking.html', dictionary)
