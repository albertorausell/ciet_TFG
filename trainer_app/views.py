from django.shortcuts import render, redirect
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
    objectivesRows = objective.objects.all().order_by('name')

    objective_form = ObjectiveForm()

    objectives_forms = []
    for data_objective in objectivesRows:
        objectives_forms.append(ObjectiveForm(instance=data_objective))

    if request.method == 'POST':
        objective_to_save = ObjectiveForm(request.POST)
        objective_to_save.save()

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
    objective_to_edit = objective.objects.get(pk=id)
    objective_form = ObjectiveForm(instance=objective_to_edit)

    dictionary = {
        'objetive_to_edit': objective_form,
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'}

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective_to_edit)
        if form.is_valid():
            acts = form.cleaned_data.get("activities")
            obj = form.save(commit=False)
            obj.activities.set(acts)
            obj.save()
        return redirect('objectives_trainer')

    return render(request, 'objectives/edit_objective.html', dictionary)
