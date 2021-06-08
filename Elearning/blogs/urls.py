from django.urls import include, path
from .views import *
app_name = "blogs"

urlpatterns = [
    path('', index, name="index"),
    path('blogs/show', show, name="show"),
]
