from django.shortcuts import render

# Create your views here.


def capabilities(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'trainer_app/templates/capabilities.html', dictionary)


def objectives(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'objectives.html', dictionary)


def statistics(request):

    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return render(request, 'statistics.html', dictionary)
