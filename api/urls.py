from django.urls import path, include

urlpatterns = [
    path('home/', include('api.home.urls')),
    path('dashbord/', include('api.dashbord.urls')),
    path('masque/', include('api.masque.urls')),
    path('staff/', include('api.staff.urls')),
]
