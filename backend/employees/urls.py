from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexView, name='index'),  # Home page
    path('employees/', views.employeesView, name='employees'),  # Employees page

]