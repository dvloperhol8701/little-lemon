from django.urls import path
from . import views

urlpatterns = [
    # This maps the root URL of your restaurant app to the index view
    path('', views.index, name='index'),
]