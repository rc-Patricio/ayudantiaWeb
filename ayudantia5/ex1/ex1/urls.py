from django.contrib import admin
from django.urls import path
from core.views import inicio, cat1, cat2, sesion, cerrar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cat1/', cat1),
    path('cat2/', cat2),
    path('sesion/', sesion, name='login'),
    path('logout/', cerrar_sesion)
]
