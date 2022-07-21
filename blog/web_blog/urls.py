from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path ('', views.about, name='about'),
    path ('login', views.login, name='login'),
    path ('contact', views.contact, name='contact'),
    path ('registration', views.registration, name='registration'),
]
