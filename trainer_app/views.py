from django.shortcuts import render, redirect
from common_app.models import training_technique, objective, capability, capability_objective, content
from .forms import Component, Contents, ObjectiveForm, CapabilityName, CapabilityDesc, CapabilityLearners, CapabilityObjectives
import json
from django.http import HttpResponse
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
    dictionary = create_base_dictionary()

    cap = capability.objects.all().order_by('name')

    cap_name = []
    cap_obj = []
    cap_stk = []
    cap_act = []
    cap_id = []

    for i in cap:
        #
        cap_name.append(i.name)
        #
        objectives_chain = ''
        objectives = capability_objective.objects.filter(capability=i.pk)
        for j in objectives:
            the_objective = objective.objects.filter(
                pk=j.objective.pk)[0]
            objectives_chain += the_objective.name + ', '
        cap_obj.append(objectives_chain[:-2])
        #
        stakeholders = i.stakeholders.all()
        stakeholders_chain = ''
        for j in stakeholders:
            stakeholders_chain += j.name + ', '
        cap_stk.append(stakeholders_chain[:-2])
        #
        cap_act.append(i.active)
        #
        cap_id.append(i.pk)

    rows = zip(cap_name, cap_obj, cap_stk, cap_act, cap_id)

    dictionary.update({
        'table': {
            'columns': ['Name', 'Objectives', 'Learners', 'Active', 'Actions'],
            'rows': rows
        }
    })

    return render(request, 'trainer_app/templates/capabilities.html', dictionary)


def cap_name(request, id_str):
    id = int(id_str)
    dictionary = create_base_dictionary()

    if request.method == 'POST':
        form = CapabilityName(request.POST)
        if form.is_valid():
            cap = capability.objects.get(pk=id)
            cap.name = form.cleaned_data.get('cap_name')
            cap.save()
            return redirect('description_and_image', id=id)
    else:
        if id == -1:
            cap = capability()
            cap.save()
            form = CapabilityName()
            dictionary.update({
                'cap_id': cap.pk,
                'form': form,
            })
        else:
            cap = capability.objects.get(pk=id)
            form = CapabilityName(initial={'cap_name': cap.name})
            dictionary.update({
                'cap_id': cap.pk,
                'form': form,
            })

        return render(request, 'capabilities/create_name.html', dictionary)

    return HttpResponse(status=204)


def cap_desc(request, id):
    dictionary = create_base_dictionary()
    cap = capability.objects.get(pk=id)

    if request.method == 'POST':
        form = CapabilityDesc(request.POST, request.FILES)
        if form.is_valid():
            cap.description = form.cleaned_data.get('cap_desc')
            cap.image = form.cleaned_data.get('cap_image')
            cap.save()
            return redirect('learners', id=id)
        else:
            if (cap.image):
                cap.description = form.cleaned_data.get('cap_desc')
                cap.save()
                return redirect('learners', id=id)
    else:
        form = CapabilityDesc(
            initial={'cap_desc': cap.description, 'cap_image': cap.image})

        dictionary.update({
            'cap_id': cap.pk, 'form': form})

        return render(request, 'capabilities/create_description.html', dictionary)

    return HttpResponse(status=204)


def cap_learners(request, id):
    dictionary = create_base_dictionary()
    cap = capability.objects.get(pk=id)

    if request.method == 'POST':
        form = CapabilityLearners(request.POST)
        if form.is_valid():
            cap.stakeholders.set(form.cleaned_data.get("stakeholders"))
            cap.save()
            return redirect('objectives', id=id)
    else:
        form = CapabilityLearners(instance=cap)
        dictionary.update({
            'cap_id': cap.pk, 'form': form
        })
        return render(request, 'capabilities/create_learners.html', dictionary)

    return HttpResponse(status=204)


def cap_objectives(request, id):
    dictionary = create_base_dictionary()
    cap = capability.objects.get(pk=id)

    if request.method == 'POST':
        form = CapabilityObjectives(request.POST)
        if form.is_valid():
            cap.objectives.set(form.cleaned_data.get("objectives"))
            cap.save()
            return redirect('contents', id=id, obj_pos=0, cont_pos=0)
    else:
        form = CapabilityObjectives(instance=cap)
        dictionary.update({
            'cap_id': cap.pk
        })

        obj_act = []
        obj_ph = []
        objectives = objective.objects.all()
        for ob in objectives:
            act_chain = ''
            ph_chain = ''
            ob_activities = ob.activities.all()
            for act in ob_activities:
                act_chain += act.name + ', '
                try:
                    ph_chain.index(act.phase.name)
                except:
                    ph_chain += act.phase.name + ', '
            obj_act.append(act_chain[:-2])
            obj_ph.append(ph_chain[:-2])

        dictionary.update({
            'obj_act': obj_act,
            'obj_ph': obj_ph,
            'form': form
        })
        return render(request, 'capabilities/create_objectives.html', dictionary)

    return HttpResponse(status=204)


def cap_contents(request, id, obj_pos, cont_pos):
    dictionary = create_base_dictionary()
    cap = capability.objects.get(pk=id)

    if request.method == 'POST':
        if '_c' in request.POST['action']:
            idObj = request.POST['action'][:-2]
            form = Contents(request.POST)
            if form.is_valid():
                objective = capability_objective.objects.filter(
                    capability=cap.pk, objective=idObj)
                cont = content()
                cont.name = form.cleaned_data.get("name")
                cont.dimension = form.cleaned_data.get("dimension")
                cont.capability_objective = objective[0]
                cont.save()
                return redirect('contents', id=id, obj_pos=int(request.POST['objMant']), cont_pos=cont_pos)

    else:
        objs = cap.objectives.all()
        dictionary.update({
            'obj_pos': obj_pos,
            'cont_pos': cont_pos,
            'cap_name': cap.name,
            'cap_id': cap.pk,
            'cap_obj': objs,
            'contentsForm': Contents(),
            'componentsForm': Component(),
        })

        obj_cont = []
        cont_tech = []
        for obj in objs:
            cap_obj = capability_objective.objects.filter(
                capability=cap.pk, objective=obj.pk)
            contents = content.objects.filter(
                capability_objective=cap_obj[0].pk)
            obj_cont.append({
                'cap_obj_pk': obj.pk,
                'contents': contents
            })
            for cont in contents:
                media_comps = training_technique.objects.filter(
                    content=cont.pk
                )
                cont_tech.append({
                    'cont': cont,
                    'media_comps': media_comps,
                })
        dictionary.update({
            'obj_cont': obj_cont,
            'cont_tech': cont_tech,
        })

        return render(request, 'capabilities/create_contents.html', dictionary)

    return HttpResponse(status=204)


def objectives(request):
    dictionary = create_base_dictionary()

    objectivesRows = objective.objects.all().order_by('name')
    dictionary.update({
        'table': {
            'columns': ['Objective', 'Actions'],
            'rows': objectivesRows
        }
    })

    objective_form = ObjectiveForm()
    dictionary.update({'objectivesForm': objective_form})

    if request.method == 'POST':
        form = ObjectiveForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'objectives.html', dictionary)


def statistics(request):
    dictionary = create_base_dictionary()
    return render(request, 'statistics.html', dictionary)


def objective_edit(request, id):
    dictionary = create_base_dictionary()

    objective_to_edit = objective.objects.get(pk=id)
    objective_form = ObjectiveForm(instance=objective_to_edit)
    dictionary.update({'objetive_to_edit': objective_form})

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective_to_edit)
        if form.is_valid():
            acts = form.cleaned_data.get("activities")
            obj = form.save(commit=False)
            obj.activities.set(acts)
            obj.save()
        return redirect('objectives_trainer')

    return render(request, 'objectives/edit_objective.html', dictionary)


def create_base_dictionary():
    dictionary = {
        'nombre': 'alberto rausell',
        'organizacion': 'Universitat Politècnica de València'
    }
    return dictionary
