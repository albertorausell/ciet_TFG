from common_app.models import learner_profile, trainer_profile
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_req(request):
    dictionary = create_base_dictionary(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            learner = learner_profile.objects.filter(user=user.pk)
            trainer = trainer_profile.objects.filter(user=user.pk)
            if len(learner) > 0 and len(trainer) > 0:
                return redirect('')
            elif len(learner) > 0:
                return redirect('capabilities_learner')
            elif len(trainer) > 0:
                return redirect('capabilities_trainer')
            else:
                dictionary.update({
                    'error': 'The user has not a trainer or learner profile'
                })
                return render(request, 'common_app/templates/login.html', dictionary)
        else:
            dictionary.update({
                'error': 'Bad username or password'
            })
            return render(request, 'common_app/templates/login.html', dictionary)
    return render(request, 'common_app/templates/login.html', dictionary)


def logout_req(request):
    dictionary = create_base_dictionary(request)
    logout(request)
    return redirect('login')


def main_page(request):
    dictionary = create_base_dictionary(request)
    return render(request, 'common_app/templates/main_page.html', dictionary)


def create_base_dictionary(request):
    dictionary = {
        'host': 'http://127.0.0.1:8000/'
    }
    return dictionary
