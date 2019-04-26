from django.shortcuts import render

# Create your views here.


def main(request):
    # content = {
    #     'title': title,
    #     'links_menu': links_menu,
    #     'same_prpducts': same_products
    # }
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
