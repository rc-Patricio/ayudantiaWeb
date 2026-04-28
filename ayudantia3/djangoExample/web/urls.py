from django.urls import path
from .views import vista1, vista2, vista3

urlpatterns = [
    path('vista1/', vista1),
    path('vista2/', vista2),
    path('vista3/', vista3),
]