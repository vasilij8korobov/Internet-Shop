from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description') # обрати внимание на "дандеры" они как точки


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id', 'name',)

