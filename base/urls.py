from django.urls import path, re_path
from . import views
app_name="base"
urlpatterns = [
    path("", views.index, name="main"),]