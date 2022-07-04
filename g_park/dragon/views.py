from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from view_wheel.models import Reporting
from dragon.models import ViewDragon, ReportingDragon


menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Cотрудники парка", 'url_name': 'personnel'},
        {'title': "История парка", 'url_name': 'history'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'},
        ]

def viev_dragon(request):
    info = ViewDragon.objects.all()
    record = ReportingDragon.objects.all().get()
    reporting = Reporting.objects.get()
    sl_home = {
        'info': info,
        'menu': menu,
        'record': record,
        'title': 'Дракоша',
        'reporting': reporting
    }
    return render(request, 'dragon/dragon.html', context=sl_home)
