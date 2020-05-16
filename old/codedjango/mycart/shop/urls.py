from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="Aboutus"),
    path("contact/",views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/",views.search, name="Search"),
    path("productview/",views.prodview, name="ProductView"),
    path("checkout/",views.checkout, name="Checkout"),
]
