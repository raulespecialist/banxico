from django.urls import path
 
from . import views
 
urlpatterns = [
    path('udis/', views.udis),
    path('usd/', views.usd),
]