from django.contrib import admin

# Internal modules
from .models import (
    Category, 
    Color,
    Product,
    StarToProduct,
    ProductImage,
    CardItem,
    Like,
    TotalCartPrice
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'parent', 'created_at')
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'category', 'price', 'created_at')
    
    
@admin.register(StarToProduct)
class StarToProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'user', 'product', 'star', 'created_at')
    
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", 'product', 'created_at')

@admin.register(CardItem)
class CardItemAdmin(admin.ModelAdmin):
    list_display = ("id", 'product', 'user', 'qty', 'created_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", 'product', 'user')

@admin.register(TotalCartPrice)
class TotalCartPriceAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')