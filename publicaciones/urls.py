from django.urls import path
from . import views

urlpatterns = [
    path('ver-publicaciones/', views.publicaciones_view, name='ver-publicaciones'),
    path('carousel/', views.carousel_view, name='carousel')

]