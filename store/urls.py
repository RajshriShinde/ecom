from django.urls import path
from .views import (product_list, product_detail, variant_list, variant_detail, image_list, image_detail
                                , collection_list, collection_detail, category_list, category_detail
                                , list_of_product_of_collections, list_of_variants_of_collection, update_email
                                , list_of_variants_of_category, send_mail_to_all_users)

urlpatterns = [
    path('product/', product_list),
    path('product_detail/<int:pk>/',  product_detail),
    path('variant/', variant_list),
    path('variant_detail/<int:pk>/', variant_detail),
    path('image/', image_list),
    path('image_detail/<int:pk>/', image_detail),
    path('collection/', collection_list),
    path('collection_detail/<int:pk>/', collection_detail),
    path('category/', category_list),
    path('category_detail/<int:pk>/', category_detail),
    path('collection/<int:pk>/product_list/', list_of_product_of_collections),
    path('collection/<int:pk>/variant_list/', list_of_variants_of_collection),
    path('category/<int:pk>/variant_list/', list_of_variants_of_category),
    path('user_email/<int:pk>/', update_email),
    path('send_mail/', send_mail_to_all_users),
]

