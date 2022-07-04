from django.urls import path
from .views import *
from p_info.views import *

#from p_info.views import view_home

urlpatterns = [
    path('', view_home, name='home'),
    path('view_wheel/', viev_viewwheel, name='view_wheel'),
    ]