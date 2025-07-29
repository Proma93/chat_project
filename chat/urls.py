from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/<str:room_name>/', views.room, name='room'),
    path('create-room/', views.create_room, name='create_room'),
    path('logout/', LogoutView.as_view(next_page='logged_out'), name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),
]