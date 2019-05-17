from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import ProductCategory, Product


context = {'title': 'Вагончик',
           'links_menu': {'main': 'Главная', 'products': 'Каталог', 'contact': 'Контакты'},
           'categories': ProductCategory.objects.all(),
           'products': Product.objects.all(),
           }


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {'title': title,
                   'links_menu': links_menu,
                   'category': category,
                   'products': products, }
        return render(request, 'mainapp/products.html', context)

    same_products = Product.objects.all()[3:5]

    context = {'title': title,
               'links_menu': links_menu,
               'same_products': same_products, }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html', context)
