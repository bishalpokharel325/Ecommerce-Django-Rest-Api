from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Primarycategory, Secondarycategory, Brand


class PrimaryCategoryResource(resources.ModelResource):
    class Meta:
        model = Primarycategory


class SecondaryCategoryResource(resources.ModelResource):
    class Meta:
        model = Secondarycategory


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


@admin.register(Primarycategory)
class AdminPrimaryCategory(ImportExportModelAdmin):
    resource_class = PrimaryCategoryResource
    list_display = ['title', 'created_by', 'created_at', 'visible']
    search_fields = ['title', 'created_by', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 10
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


@admin.register(Secondarycategory)
class AdminSecondaryCategory(ImportExportModelAdmin):
    resource_class = SecondaryCategoryResource
    list_display = ['title', 'created_by', 'created_at', 'visible', 'primary_category']
    search_fields = ['title', 'created_by', 'created_at']
    date_hierarchy = 'created_at'
    sortable_by = ['created_at', 'title', 'visible', 'primary_category', 'created_by']
    list_per_page = 10
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


@admin.register(Category)
class AdminCategory(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ['title', 'created_by', 'created_at', 'visible', 'secondary_category']
    search_fields = ['title', 'created_by', 'created_at']
    date_hierarchy = 'created_at'
    sortable_by = 'created_at'
    list_per_page = 10
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


@admin.register(Brand)
class AdminBrand(ImportExportModelAdmin):
    resource_class = BrandResource
    list_display = ['title', 'created_by', 'created_at', 'visible']
    search_fields = ['title', 'created_by', 'created_at']
    date_hierarchy = 'created_at'
    sortable_by = 'created_at'
    list_per_page = 10
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
