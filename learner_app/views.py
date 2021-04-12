from django.shortcuts import render, HttpResponse
from CiET.variables import Variables

# Create your views here.


def capabilities(request):

    return render(request, 'home.html', {'nombre': 'rausell'})


def evaluations(request):

    return HttpResponse('Evaluations')


def ranking(request):

    return HttpResponse('Ranking')
