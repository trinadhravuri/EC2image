from django.urls import path
from . import views



urlpatterns = [
    path('',views.allmyimages,name='allmyimages')
] 
