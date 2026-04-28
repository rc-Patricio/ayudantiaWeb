from django.contrib import admin
from django.urls import path
from core.views import inicio, nosotros, alumnos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('alumnos/', alumnos),
    path('nosotros/', nosotros),
]
