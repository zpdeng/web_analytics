from django.urls import path 
from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', views.home, name='dashboard-home'),
	path('about/', views.about, name='dashboard-about'),
	path('charts/', views.charts, name='dashboard-charts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()