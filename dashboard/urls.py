from django.urls import path 
from . import views

urlpatterns = [
	path('', views.home, name='dashboard-home'),
	path('about/', views.about, name='dashboard-about'),
	path('charts/', views.charts, name='dashboard-charts'),
]
