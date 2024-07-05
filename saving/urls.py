from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('move-money/', views.move_money_view, name='move-money'),
]