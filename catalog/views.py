from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Product


# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/home.html', context=context)
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#
#         return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
#     return render(request, 'catalog/contacts.html')
#
#
# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context=context)

class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

