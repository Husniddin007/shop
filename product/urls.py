from django.urls import path
from product import views

urlpatterns = [
    path('list/',views.product_list,name='product_list'),
    path('detail/<int:product_id>/',views.product_detail,name='product_detail'),
    path('about/',views.about,name='about'),
]