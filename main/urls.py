from django.urls import path
from . import views

# URLS 

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("team/", views.team , name="team")
]