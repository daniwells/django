from django.urls import path
from . import views

app_name = 'colaborators'

urlpatterns = [
    path('', views.show_colaborators, name="show_colaborators"),
    path('colaborators/', views.show_colaborators, name="show_colaborators"),
]