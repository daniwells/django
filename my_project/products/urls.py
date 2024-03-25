from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.show_products, name="show_products"),
    path('products/', views.show_products, name="show_products"),
    path('new/', views.register_product, name="register_product"),
    path('new/post', views.show_products, name="show_products"),
    path('edit/<int:pk>', views.edit_product, name="edit_product"),
    path('delete/<int:pk>', views.delete_product, name="delete_product"),
    # path('delete/<int:pk>', views.delete_client, name="delete_client"),
]