from django.urls import path

from . import views

urlpatterns=[
    path("",views.products,name="products"),
    path("/post",views.postProducts,name="products"),
    path("/productdetails/<slug:slug>",views.productdetails,name="productdetails"),
]