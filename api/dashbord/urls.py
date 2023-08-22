from django.urls import path, include
from . import views

urlpatterns = [
    path('create/country', views.create_country),
    path('update/country/<int:pk>', views.update_country),
    path('delate/country/<int:pk>', views.delate_country),
    path('create/city', views.create_city),
    path('update/city/<int:pk>', views.update_city),
    path('delate/city/<int:pk>', views.delate_city),
    path('masque/create', views.create_masque),
    path('masque/update/<int:pk>', views.update_masque),
    path('masque/delate/<int:pk>', views.delate_masque),
    path('create/staff', views.create_staff),
    path('update/staff/<int:pk>', views.update_staff),
    path('delate/staff/<int:pk>', views.delate_staff),
]
