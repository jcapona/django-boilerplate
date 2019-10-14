from django.urls import path
from django.urls import include
from django_boilerplate.apps.home.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

