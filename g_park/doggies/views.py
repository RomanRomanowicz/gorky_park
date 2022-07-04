from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from view_wheel.models import Reporting
from doggies.models import ViewDoggies, ReportingDoggies


menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Cотрудники парка", 'url_name': 'personnel'},
        {'title': "История парка", 'url_name': 'history'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'},
        ]

def viev_doggies(request):
    info = ViewDoggies.objects.all()
    record = ReportingDoggies.objects.all().get()
    reporting = Reporting.objects.get()
    sl_home = {
        'info': info,
        'menu': menu,
        'record': record,
        'title': 'Собачки',
        'reporting': reporting
    }
    return render(request, 'doggies/doggies.html', context=sl_home)
