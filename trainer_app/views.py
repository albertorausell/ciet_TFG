from django.shortcuts import render
from common_app.models import objective
from .forms import ObjectiveForm

# Create your views here.

# ctrl+shift+p > Preferences: Configure Language Specific Settings > Python
# {
#    "python.linting.pylintArgs": [
#        "--load-plugins=pylint_django"
#    ],
#
#    "[python]": {
#
#    }
# }
# https://stackoverflow.com/questions/45135263/class-has-no-objects-member


def capabilities(request):
    dictionary = {
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }

    return render(request, 'trainer_app/templates/capabilities.html', dictionary)


def objectives(request):
    objectivesRows = []

    objective_form = ObjectiveForm()

    if request.method == 'POST':
        objective_to_save = ObjectiveForm(request.POST)
        objective_to_save.save()

    for obj in objective.objects.raw("""
        select *
        from common_app_objective cao 
        """):
        objectivesRows.append([obj.name, 'Edit'])

    dictionary = {
        'table': {
            'columns': ['Name', 'Actions'],
            'rows': objectivesRows
        },
        'objectivesForm': objective_form,
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
