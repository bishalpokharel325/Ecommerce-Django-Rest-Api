from django.urls import path

from . import views

urlpatterns=[
    path("",views.categories,name="categories"),
    path("post", views.postCategory, name="postcategories"),
    path("/primarycategories", views.getPrimaryCategory, name="getprimarycategories"),
    path("/primarycategories/<int:id>", views.getPrimaryCategoryDetails, name="getprimarycategories"),
    path("/primarycategories/<int:id>/<int:sec_id>", views.getCategoryDetails, name="getcategories"),
]