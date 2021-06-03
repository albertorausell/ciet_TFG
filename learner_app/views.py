from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse
from common_app.models import exercise, learner_profile, organization, question, answer, training_technique, objective, capability, capability_objective, content
from CiET.variables import Variables

# Create your views here.


def is_learner(user):
    try:
        return learner_profile.objects.filter(user=user.pk)[0].rol.isLearner
    except:
        return False


@login_required(redirect_field_name=None)
@user_passes_test(is_learner, login_url='/trainer/capabilities', redirect_field_name=None)
def capabilities(request):
    dictionary = create_base_dictionary(request)

    check_caps = capability.objects.filter(
        active=True, organization=dictionary['org'])
    pending_caps = []

    for cap in check_caps:
        if dictionary['learner'].rol in cap.stakeholders.all():
            pending_caps.append(cap)

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


@login_required(redirect_field_name=None)
@user_passes_test(is_learner, login_url='/trainer/capabilities', redirect_field_name=None)
def capability_details(request, id):
    dictionary = dictionary = create_base_dictionary(request)
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


@login_required(redirect_field_name=None)
@user_passes_test(is_learner, login_url='/trainer/capabilities', redirect_field_name=None)
def evaluations(request):

    dictionary = create_base_dictionary(request)
    return render(request, 'evaluations.html', dictionary)


@login_required(redirect_field_name=None)
@user_passes_test(is_learner, login_url='/trainer/capabilities', redirect_field_name=None)
def ranking(request):

    dictionary = dictionary = create_base_dictionary(request)
    return render(request, 'ranking.html', dictionary)


def create_base_dictionary(request):
    user = request.user
    name_to_display = user.first_name + ' ' + user.last_name
    if name_to_display == ' ':
        name_to_display = user.username

    learner = learner_profile.objects.get(user=user.pk)
    dictionary = {
        'name': name_to_display,
        'org': learner.organization,
        'learner': learner,
        'host': 'http://127.0.0.1:8000/'
    }
    return dictionary
