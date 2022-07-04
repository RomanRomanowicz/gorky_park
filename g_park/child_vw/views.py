from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from p_info.models import InfoPersonnel
from child_vw.models import ViewChild_vw
from child_vw.models import ReportingChild_vw


menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Cотрудники парка", 'url_name': 'personnel'},
        {'title': "История парка", 'url_name': 'history'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'},
        ]

def viev_child_vw(request):
    info = ViewChild_vw.objects.all()
    record = InfoPersonnel.objects.all().get(pk=2)
    reporting = ReportingChild_vw.objects.get()
    sl_home = {
        'info': info,
        'menu': menu,
        'record': record,
        'title': 'Детское колесо обозрения',
        'reporting': reporting
    }
    return render(request, 'child_vw/child_vw.html', context=sl_home)
    #return HttpResponse(record)