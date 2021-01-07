from django.urls import path

from .views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view,product_list_view, product_update_view

app_name = 'products'
urlpatterns = [
 
    #path('initial/',render_initial_data),
    #path('products/<int:my_id>/', dynamic_lookup_view, name = 'product-detail'),

    path('', product_list_view, name='product-delete'),
    path('create/',product_create_view, name = 'product-create'),    
    path('<int:my_id>/',product_detail_view, name = 'product-detail'),
    path('<int:my_id>/delete/', product_update_view, name='product-update'),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),

]