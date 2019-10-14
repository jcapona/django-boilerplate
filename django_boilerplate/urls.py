from django.urls import path
from django.urls import include


urlpatterns = [
    path('accounts/', include('django_boilerplate.apps.accounts.urls')),
    path('', include('django_boilerplate.apps.home.urls')),
]

