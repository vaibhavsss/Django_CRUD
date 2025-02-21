from django.urls import path
from . import views 

urlpatterns = [
    path("", views.clothing, name="clothing"), 
]