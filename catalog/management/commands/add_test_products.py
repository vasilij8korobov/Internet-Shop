from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test students to the database'

    def handle(self, *args, **kwargs):
        #Удаление данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создайте категории
        electronics = Category.objects.create(name='Электроника')
        books = Category.objects.create(name='Книги')
        clothing = Category.objects.create(name='Одежда')

        # Создайте продукты
        Product.objects.create(name='Лаптоп', price=1000, category=electronics)
        Product.objects.create(name='Смартфон', price=800, category=electronics)
        Product.objects.create(name='Приключения Швейки', price=20, category=books)
        Product.objects.create(name='Майка', price=15, category=clothing)

        self.stdout.write(self.style.SUCCESS('Successfully added test products'))

