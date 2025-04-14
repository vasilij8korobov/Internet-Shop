from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    """Возвращает список всех продуктов в указанной категории."""
    return Product.objects.filter(category_id=category_id, is_published=True)


def get_cached_products():
    cache_key = 'all_products'
    products = cache.get(cache_key)
    if products is None:
        products = Product.objects.filter(is_published=True)
        cache.set(cache_key, products, 60 * 15)
    return products
