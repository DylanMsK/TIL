from django.urls import path
from . import views

app_name = 'shouts'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/update/', views.update, name="update"),
    path('create/', views.create, name='create')
]