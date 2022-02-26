from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('back', views.back_view, name='back'),
    path('enc_dec', views.enc_dec_view, name='enc_dec')
]