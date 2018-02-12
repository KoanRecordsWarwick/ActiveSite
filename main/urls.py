from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('news/', views.news, name="news"),
	path('artists/', views.artists, name="artists"),
	path('releases/', views.releases, name="releases"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('test/', views.test, name="test"),
]
