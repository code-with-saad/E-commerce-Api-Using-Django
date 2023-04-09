from django.urls import path
from . import views

urlpatterns = [
    path("showcart/", views.cartview)
]