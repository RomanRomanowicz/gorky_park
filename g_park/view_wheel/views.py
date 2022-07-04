from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from view_wheel.models import ViewWheel
from p_info.models import InfoPersonnel
from view_wheel.models import Reporting

menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Cотрудники парка", 'url_name': 'personnel'},
        {'title': "История парка", 'url_name': 'history'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'},
        ]

def viev_viewwheel(request):
    info = ViewWheel.objects.all()
    record = InfoPersonnel.objects.all().get(pk=2)
    reporting = Reporting.objects.get()
    sl_home = {
        'info': info,
        'menu': menu,
        'record': record,
        'title': 'Колесо обзора',
        'reporting': reporting
    }
    return render(request, 'view_wheel/view_wheel.html', context=sl_home)
    #return HttpResponse(record)