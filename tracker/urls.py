from django.urls import path
from . import views

urlpatterns = [
    # Map the root address of the app to the memorial_home view function
    path('', views.memorial_home, name="home"),
]
