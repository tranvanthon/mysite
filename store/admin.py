from django.contrib import admin
from store.models import Category, ProductImage, Product




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields": ["name"]}),
        ("Icon code", {"fields": ["icon_code"]}),
        ("Images", {"fields": ["image"]}),  # Thêm field image
        ("Status", {"fields": ["is_active", "is_featured", "display_order"]}),
    ]
    list_display = ["name", "is_active", "display_order"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
