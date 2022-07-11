from django.urls import path
from .views import *

urlpatterns = [
    path('', view_home, name='home'),
    path('personnel/', view_personnel, name='personnel'),
    path('history/', view_history, name='history'),
    path('login/', view_login, name='login'),
    path('photo/', view_photo, name='photo'),
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)