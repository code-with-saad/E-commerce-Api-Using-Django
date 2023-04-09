from django.urls import path
from . import views

urlpatterns = [
    # path("", views.cartview),
    path("create/", views.post)
]