from django.http import HttpResponse
from CiET.variables import Variables
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


def saludo(request):

    nombre = 'rausell'
    return render(request, 'index.html', {'nombre': nombre})


def getDate(request):
    actualDate = datetime.datetime.now()
    document = 'Fecha y hora: %s' % actualDate
    return HttpResponse(document)


def ageCalculator(request, age, year):
    actualAge = age
    period = year - 2021
    futureAge = actualAge + period
    document = 'En el año %s tendras %s años' % (year, futureAge)

    return HttpResponse(document)
