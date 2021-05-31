from django.shortcuts import render, HttpResponse
from common_app.models import exercise, question, answer, training_technique, objective, capability, capability_objective, content
from CiET.variables import Variables

# Create your views here.


def capabilities(request):
    dictionary = dictionary = create_base_dictionary()

    pending_caps = capability.objects.filter(active=True)
    details_caps = []
    for cap in pending_caps:
        objectives = capability_objective.objects.filter(capability=cap.pk)
        objective_number = len(objectives)
        contents_number = 0
        for objective in objectives:
            contents = content.objects.filter(
                capability_objective=objective.pk)
            contents_number += len(contents)
        details_caps.append({
            'details': cap,
            'contents_number': contents_number,
            'objective_number': objective_number
        })
    dictionary.update({
        'pending_caps': details_caps,
    })

    return render(request, 'learner_app/templates/capabilities.html', dictionary)


def capability_details(request, id):
    dictionary = dictionary = create_base_dictionary()
    cap = capability.objects.get(pk=id)
    objs = capability_objective.objects.filter(capability=id)
    objs_list = []
    for obj in objs:
        contents_number = len(content.objects.filter(
            capability_objective=obj.pk))
        objective_name = obj.objective.name
        objs_list.append({
            'name': objective_name,
            'contents_number': contents_number,
        })

    dictionary.update({
        'cap': cap,
        'objs': objs_list
    })

    return render(request, 'learner_app/templates/capabilities/details.html', dictionary)


def evaluations(request):

    dictionary = create_base_dictionary()
    return render(request, 'evaluations.html', dictionary)


def ranking(request):

    dictionary = dictionary = create_base_dictionary()
    return render(request, 'ranking.html', dictionary)


def create_base_dictionary():
    dictionary = {
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València',
        'host': 'http://127.0.0.1:8000/'
    }
    return dictionary
