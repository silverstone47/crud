from django.urls import path
from . import views

urlpatterns = [
    path('user', views.userApi),
    path('user/<int:id>', views.userApi),
]
