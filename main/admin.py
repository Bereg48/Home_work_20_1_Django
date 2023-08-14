from django.contrib import admin

from main.models import Category, Product, Version
from users.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name_current_version', 'name_version',)
    list_filter = ('name_current_version',)


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'country', 'avatar', 'email_verify')
    list_filter = ('country',)
    search_fields = ('country', 'email',)
