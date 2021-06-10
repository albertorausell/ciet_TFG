import math
from trainer_app.views import cap_learners
from CiET.variables import Variables
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render, HttpResponse
from common_app.models import capability_learner, evaluation, exercise, learner_profile, organization, question, answer, training_technique, objective, capability, capability_objective, content
content_model = content

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
    finished_caps = []

    for cap in check_caps:
        cap_learner = capability_learner.objects.filter(
            capability=cap.pk, learner_profile=dictionary['learner'])
        if len(cap_learner) > 0:
            if cap_learner[0].pending:
                pending_caps.append(cap)
            else:
                finished_caps.append(cap)
        else:
            if dictionary['learner'].rol in cap.stakeholders.all():
                pending_caps.append(cap)

    # TO-DO: check if cap is pending in order to show it

    details_pending_caps = []
    for cap in pending_caps:
        objectives = capability_objective.objects.filter(capability=cap.pk)
        objective_number = len(objectives)
        contents_number = 0
        for objective in objectives:
            contents = content.objects.filter(
                capability_objective=objective.pk)
            contents_number += len(contents)
        details_pending_caps.append({
            'details': cap,
            'contents_number': contents_number,
            'objective_number': objective_number
        })
    details_finished_caps = []
    for cap in finished_caps:
        objectives = capability_objective.objects.filter(capability=cap.pk)
        objective_number = len(objectives)
        contents_number = 0
        for objective in objectives:
            contents = content.objects.filter(
                capability_objective=objective.pk)
            contents_number += len(contents)
        details_finished_caps.append({
            'details': cap,
            'contents_number': contents_number,
            'objective_number': objective_number
        })
    dictionary.update({
        'pending_caps': details_pending_caps,
        'finished_caps': details_finished_caps,
    })

    return render(request, 'learner_app/templates/capabilities.html', dictionary)


@login_required(redirect_field_name=None)
@user_passes_test(is_learner, login_url='/trainer/capabilities', redirect_field_name=None)
def capability_show(request, id):
    dictionary = create_base_dictionary(request)
    cap = capability.objects.get(pk=id)
    objs = cap.objectives.all()

    obj_cont = []
    cont_tech = []
    cont_pos = 0

    # FOR EVALUATIONS
    last_pk_obj = -1
    if len(objs) > 0:
        last_pk_obj = objs[len(objs) - 1].pk
    # ---------------

    for obj in objs:
        cap_obj = capability_objective.objects.filter(
            capability=cap.pk, objective=obj.pk)
        contents = content_model.objects.filter(
            capability_objective=cap_obj[0].pk)
        contents_with_pos = []

        # FOR EVALUATIONS
        lastObj = False
        if obj.pk == last_pk_obj:
            lastObj = True

        last_pk_cont = -1
        if len(contents) > 0:
            last_pk_cont = contents[len(contents) - 1].pk
        # ---------------

        for cont in contents:
            media_comps = training_technique.objects.filter(
                content=cont.pk
            ).select_subclasses()

            # FOR EVALUATIONS
            lastCont = False
            if cont.pk == last_pk_cont:
                lastCont = True
            # ---------------

            cont_tech.append({
                'cont': cont,
                'media_comps': orderComps(media_comps),
                'isLastCont': lastCont,
                'isLastObj': lastObj
            })
            contents_with_pos.append({
                'object': cont,
                'pos': cont_pos
            })
            cont_pos += 1

        obj_cont.append({
            'obj_pk': obj.pk,
            'cap_obj_pk': cap_obj[0].pk,
            'name': obj.name,
            'contents': contents_with_pos
        })
    dictionary.update({
        'obj_cont': obj_cont,
        'cont_tech': cont_tech,
        'cap': cap,
        'showMark': False
    })

    # last content logic
    cap_learner = capability_learner.objects.filter(
        capability=cap.pk, learner_profile=dictionary['learner'].pk)
    current_content = 0
    if len(cap_learner) == 0:
        new_cap_learner = capability_learner()
        new_cap_learner.capability = cap
        new_cap_learner.learner_profile = dictionary['learner']
        new_cap_learner.save()
    else:
        current_content = cap_learner[0].last_content_done

    dictionary.update({
        'current_content': cont_tech[current_content]['cont'].pk,
        'current_content_pos': current_content,
    })
    # ------------------

    if request.method == 'POST':
        cap_learner = capability_learner.objects.filter(
            capability=cap.pk, learner_profile=dictionary['learner'].pk)[0]
        current_content = cap_learner.last_content_done

        if 'content' in request.POST['from']:

            # check if content has evaluations
            content = cont_tech[current_content]['cont']
            cont_exercise = exercise.objects.filter(
                scope='co', referenceId=content.pk)
            if len(cont_exercise) > 0:
                unlessOneQuestion = question.objects.filter(
                    exercise=cont_exercise[0].pk)
                cont_evaluation = evaluation.objects.filter(
                    exercise=cont_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                if len(cont_evaluation) == 0 and len(unlessOneQuestion) > 0:
                    questions = getExerciseDetails(cont_exercise[0].pk)
                    dictionary.update({
                        'exercise': questions
                    })
                    return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # check if objective has evaluations
            if cont_tech[current_content]['isLastCont']:
                obj_exercise = exercise.objects.filter(
                    scope='ob', referenceId=content.capability_objective.pk)
                if len(obj_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=obj_exercise[0].pk)
                    obj_evaluation = evaluation.objects.filter(
                        exercise=obj_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(obj_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(obj_exercise[0].pk)
                        dictionary.update({
                            'exercise': questions
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # check if plan has evaluations
            if cont_tech[current_content]['isLastCont'] and cont_tech[current_content]['isLastObj']:
                cap_exercise = exercise.objects.filter(
                    scope='ca', referenceId=content.capability_objective.capability.pk)
                if len(cap_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=cap_exercise[0].pk)
                    cap_evaluation = evaluation.objects.filter(
                        exercise=cap_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(cap_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(cap_exercise[0].pk)
                        dictionary.update({
                            'exercise': questions
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            cap_learner.last_content_done += 1
            cap_learner.save()

        if 'exercise' in request.POST['from']:

            # MANAGE evaluation
            exrc = exercise.objects.get(pk=request.POST['exercise'])
            questions = getExerciseDetails(exrc.pk)
            corrects = 0
            incorrects = 0
            for ques in questions['questions']:
                for ans in ques['answers']:
                    string = str(ans.pk) + '-answer'
                    isCorrect = ans.isCorrect
                    # correction
                    checked = string in request.POST
                    if isCorrect == checked:
                        corrects += 1
                    else:
                        incorrects += 1

            mark = (corrects / (incorrects + corrects)) * 10
            if mark >= 5:
                ev = evaluation()
                ev.pending = False
                ev.mark = mark
                ev.exercise = exrc
                ev.learner_profile = dictionary['learner']
                ev.save()
                dictionary.update({
                    'showMark': True,
                    'mark': truncate(mark, 2)
                })
            else:
                ev = evaluation()
                ev.pending = True
                ev.mark = mark
                ev.exercise = exrc
                ev.learner_profile = dictionary['learner']
                ev.save()
                dictionary.update({
                    'showMark': True,
                    'mark': truncate(mark, 2)
                })
                return render(request, 'learner_app/templates/capabilities/show_content.html', dictionary)
            # ------------------------------------------------------

            # check if objective has evaluations
            content = cont_tech[current_content]['cont']
            if cont_tech[current_content]['isLastCont']:
                obj_exercise = exercise.objects.filter(
                    scope='ob', referenceId=content.capability_objective.pk)
                if len(obj_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=obj_exercise[0].pk)
                    obj_evaluation = evaluation.objects.filter(
                        exercise=obj_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(obj_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(obj_exercise[0].pk)
                        if request.POST['finished'] == 'yes':
                            dictionary.update({
                                'finished': 'yes'
                            })
                        dictionary.update({
                            'exercise': questions,
                            'showMark': True,
                            'mark': truncate(mark, 2)
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # check if plan has evaluations
            if cont_tech[current_content]['isLastCont'] and cont_tech[current_content]['isLastObj']:
                cap_exercise = exercise.objects.filter(
                    scope='ca', referenceId=content.capability_objective.capability.pk)
                if len(cap_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=cap_exercise[0].pk)
                    cap_evaluation = evaluation.objects.filter(
                        exercise=cap_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(cap_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(cap_exercise[0].pk)
                        if request.POST['finished'] == 'yes':
                            dictionary.update({
                                'finished': 'yes'
                            })
                        dictionary.update({
                            'exercise': questions,
                            'showMark': True,
                            'mark': truncate(mark, 2)
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            if request.POST['finished'] != 'yes':
                cap_learner.last_content_done += 1
                cap_learner.save()
            else:
                finish_plan(cap_learner.pk)
                return redirect('capabilities_learner')
            # ------------------------------------------------------

        if 'finish' in request.POST['from']:

            # check if content has evaluations
            content = cont_tech[current_content]['cont']
            cont_exercise = exercise.objects.filter(
                scope='co', referenceId=content.pk)
            if len(cont_exercise) > 0:
                unlessOneQuestion = question.objects.filter(
                    exercise=cont_exercise[0].pk)
                cont_evaluation = evaluation.objects.filter(
                    exercise=cont_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                if len(cont_evaluation) == 0 and len(unlessOneQuestion) > 0:
                    questions = getExerciseDetails(cont_exercise[0].pk)
                    dictionary.update({
                        'exercise': questions,
                        'finished': 'yes',
                    })
                    return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # check if objective has evaluations
            if cont_tech[current_content]['isLastCont']:
                obj_exercise = exercise.objects.filter(
                    scope='ob', referenceId=content.capability_objective.pk)
                if len(obj_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=obj_exercise[0].pk)
                    obj_evaluation = evaluation.objects.filter(
                        exercise=obj_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(obj_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(obj_exercise[0].pk)
                        dictionary.update({
                            'exercise': questions,
                            'finished': 'yes',
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # check if plan has evaluations
            if cont_tech[current_content]['isLastCont'] and cont_tech[current_content]['isLastObj']:
                cap_exercise = exercise.objects.filter(
                    scope='ca', referenceId=content.capability_objective.capability.pk)
                if len(cap_exercise) > 0:
                    unlessOneQuestion = question.objects.filter(
                        exercise=cap_exercise[0].pk)
                    cap_evaluation = evaluation.objects.filter(
                        exercise=cap_exercise[0].pk, pending=False, learner_profile=dictionary['learner'])
                    if len(cap_evaluation) == 0 and len(unlessOneQuestion) > 0:
                        questions = getExerciseDetails(cap_exercise[0].pk)
                        dictionary.update({
                            'exercise': questions,
                            'finished': 'yes',
                        })
                        return render(request, 'learner_app/templates/capabilities/show_exercise.html', dictionary)
            # ---------------

            # TO-DO: mark cap as not pending if all evaluations are passed
            finish_plan(cap_learner.pk)
            return redirect('capabilities_learner')

    # last content logic
    cap_learner = capability_learner.objects.filter(
        capability=cap.pk, learner_profile=dictionary['learner'].pk)
    current_content = 0
    if len(cap_learner) == 0:
        new_cap_learner = capability_learner()
        new_cap_learner.capability = cap
        new_cap_learner.learner_profile = dictionary['learner']
        new_cap_learner.save()
    else:
        current_content = cap_learner[0].last_content_done

    dictionary.update({
        'current_content': cont_tech[current_content]['cont'].pk,
        'current_content_pos': current_content,
    })
    # ------------------

    return render(request, 'learner_app/templates/capabilities/show_content.html', dictionary)


def finish_plan(id):
    cap_learner = capability_learner.objects.get(pk=id)
    cap_learner.pending = False
    cap_learner.save()


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def getExerciseDetails(id):
    questions = question.objects.filter(exercise=id)
    exer = exercise.objects.get(pk=id)
    name = ''
    if exer.scope == 'ca':
        ca = capability.objects.get(pk=exer.referenceId)
        name = 'Capability plan:   ' + ca.name
    elif exer.scope == 'co':
        co = content.objects.get(pk=exer.referenceId)
        name = 'Content:   ' + co.name
    else:
        ob = capability_objective.objects.get(pk=exer.referenceId)
        name = 'Objective:   ' + ob.objective.name

    res = []
    for ques in questions:
        answers = answer.objects.filter(question=ques.pk)
        res.append({
            'question': ques,
            'answers': answers
        })
    return {
        'name': name,
        'questions': res,
    }


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


def orderComps(comps):
    res = []
    for comp in comps:
        if len(res) == 0:
            res.append(comp)
        else:
            i = 0
            inserted = False
            for element in res:
                if (not inserted and comp.order < element.order):
                    res.insert(i, comp)
                    inserted = True
                i = i + 1
            if (not inserted):
                res.append(comp)

    return res


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
