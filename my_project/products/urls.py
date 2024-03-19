from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.list_client, name="show_products"),
    path('products/', views.list_client, name="show_products"),
    path('new/', views.register_client, name="register_product"),
    path('new/post', views.register_product, name="register_product"),
    path('edit/<int:pk>', views.edit_product, name="edit_product"),
    path('delete/<int:pk>', views.delete_product, name="delete_product"),
    # path('delete/<int:pk>', views.delete_client, name="delete_client"),
]