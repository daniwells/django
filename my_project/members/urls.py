from django.urls import path
from . import views

app_name = "clients"

urlpatterns = [
    path('', views.list_client, name="list_client"),
    path('clients/', views.list_client, name="list_client"),
    path('new/', views.register_client, name="register_client"),
    path('new/post', views.register_client, name="register_client"),
    path('edit/<int:pk>', views.edit_client, name="edit_client"),
    path('delete/<int:pk>', views.delete_client, name="delete_client"),
    # path('delete/<int:pk>', views.delete_client, name="delete_client"),
]