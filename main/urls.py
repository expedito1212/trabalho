from urllib.parse import urlparse
from django.urls import path
from .views import HomeView
urlparse=[
    path('', HomeView.as_view(), name='home' )
]