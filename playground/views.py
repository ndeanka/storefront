from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    # queryset = Product.objects.filter(unit_price__range=(20,40))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(inventory__lte=10)
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset = Order.objects.filter(customer__id=1)

    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20)).order_by('title')[:40]

    # products = Product.objects.values('id', 'title', 'collection__title')

    queryset = Product.objects.filter(
        id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')



    # return render(request, 'hello.html', {'name': 'William', 'products': list(queryset)})
    return render(request, 'hello.html', {'name': 'William', 'products': list(queryset)})

