from django.urls import path
from Home import views

urlpatterns = [
    path('/', views.home),
    path('show/', views.show),
    path('send/', views.send),
    path('edit/', views.edit),
    path('delete/', views.delete),
    path('recordedited/', views.recordedited),
]