from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('helpless-list/', views.HelplessListView.as_view()),
    path('helpless/<int:pk>', views.HelplessDetailView.as_view()),
    path('blogs/', views.BlogListView.as_view()),
    path('blog/<int:pk>', views.BlogDetailView.as_view()),

]