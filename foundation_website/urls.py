from django.urls import path

from . import views

app_name = 'foundation_website'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path('projects/medici', views.medici, name='medici'),
]
