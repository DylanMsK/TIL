from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('check/<int:id>', views.check, name='check'),
    path('delete/<int:id>', views.delete, name='delete'),
]
