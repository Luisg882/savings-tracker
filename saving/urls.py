from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('move-money/', views.move_money_view, name='move-money'),
    path('open-pot/', views.create_saving_pot_view, name='open-pot'),
    path('saving-pot/<int:pot_id>/', views.saving_pot_details_view, name='saving-pot-details'),
    path('close-pot/<int:pot_id>/', views.close_pot_confirmation_view, name='close-pot'),
]