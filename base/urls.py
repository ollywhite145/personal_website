from django.urls import path
from . import views



urlpatterns = [
		path('', views.home, name="home"),
		path('about/', views.about, name="about"),
		path('resume/', views.resume, name="resume"),
		path('portfolio/', views.portfolio, name="portfolio"),
		path('academics/', views.academics, name="academics"),
		path('rugby/', views.rugby, name="rugby"),
		path('contact/', views.contact, name="contact"),
]