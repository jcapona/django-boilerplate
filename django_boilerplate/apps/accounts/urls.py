from django.urls import path
from django.urls import include
from django_boilerplate.apps.accounts.views import signup


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
]

