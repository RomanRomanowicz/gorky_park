from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Cотрудники парка", 'url_name': 'personnel'},
        {'title': "История парка", 'url_name': 'history'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Войти", 'url_name': 'login'},
        ]

# Create your views here.
def view_home(request):
    info = InfoPark.objects.all()
    sl_home = {'info': info, 'menu': menu, 'title': 'ПАРК ГОРЬКОГО'}
    return render(request, 'p_info/home.html', context=sl_home)

def view_personnel(request):
    info = InfoPersonnel.objects.all()
    sl_personnel = {'info': info, 'menu': menu, 'title': 'Контакты'}
    return render(request, 'p_info/personnel.html', context=sl_personnel)

def view_history(request):
    info = InfoHistory.objects.all()
    sl_history = {'info': info, 'menu': menu, 'title': 'История парка'}
    return render(request, 'p_info/history.html', context=sl_history)

def view_login(request):
    sl_login = {'menu': menu, 'title': 'login'}
    return render(request, 'p_info/login.html', context=sl_login)

def view_photo(request):
    sl_login = {'menu': menu, 'title': 'Фотогалерея'}
    return render(request, 'p_info/photo.html', context=sl_login)
