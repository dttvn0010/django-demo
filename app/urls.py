from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='home'),
    path('map_view', mapView, name='map-view'),
    path('accounts/', include('django.contrib.auth.urls')),                 # new
]

