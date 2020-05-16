from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageViewer.as_view(), name="home"),
]
