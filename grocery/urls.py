from django.urls import path

from flipkart import grocery
from flipkart.grocery import views

urlpatterns = [
    path('grocery/', views,grocery, name="grocery")
    
]