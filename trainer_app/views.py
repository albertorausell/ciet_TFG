from django.shortcuts import render
from common_app.models import objective, capability
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
    capabilitiesRows = capability.objects.all()
    dictionary = {
        'table': {
            'columns': ['Name', 'Objectives', 'Learners', 'Active', 'Actions'],
            'rows': capabilitiesRows
        },
        'isTrainer': False,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }

    return render(request, 'trainer_app/templates/capabilities.html', dictionary)


def objectives(request):
    objectivesRows = objective.objects.all()

    objective_form = ObjectiveForm()

    if request.method == 'POST':
        objective_to_save = ObjectiveForm(request.POST)
        objective_to_save.save()

    objectives_forms = []
    for data_objective in objectivesRows:
        objectives_forms.append(ObjectiveForm(instance=data_objective))

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


def objective_edit(request, id):
    objective = objective.objects.get(pk=id)
    objective_to_edit = ObjectiveForm(objective)

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective)

    return
