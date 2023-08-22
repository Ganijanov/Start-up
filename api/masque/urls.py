from django.urls import path, include
from . import views

urlpatterns = [
    path('masque/list', views.list_masques),
    path('masque/detail/<int:pk>', views.masque_detail),
    
]
