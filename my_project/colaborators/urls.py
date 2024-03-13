from django.urls import path
from . import views

app_name = 'colaborators'

urlpatterns = [
    path('', views.show_colaborators, name="show_colaborators"),
    path('colaborators/', views.show_colaborators, name="show_colaborators"),
    path('new/', views.make_colaborator, name="make_colaborator"),
    path('new/post', views.make_colaborator, name="make_colaborator"),
    path('edit/<int:pk>', views.edit_colaborator, name="edit_colaborator"),
    path('delete/<int:pk>', views.delete_colaborator, name="delete_colaborator"),
]