import re
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem


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
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.prefetch_related(
        # 'orderitem_set__product').select_related('customer').order_by('-placed_at')[:5]

    # counts = Product.objects.aggregate(count=Count('id'))

    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    # queryset = Product.objects.filter(
    #     id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')

    # return render(request, 'hello.html', {'name': 'William', 'products': list(queryset)})
    # return render(request, 'hello.html', {'name': 'William', 'order': list(queryset)})

    return render(request, 'hello.html', {'name': 'William', 'products': list(queryset)})


def zoezi(request):
    result = OrderItem.objects.filter('product__id').aggregate(count=Count('id'))
    return render(request, 'hello.html', {'result': result})
    

def create_data(request):
    collection = Collection()
    collection.title = 'Video game'
    collection.featured_product = Product(pk=1)
    collection.save()
    return render(request, 'create_data.html', {'collection': collection})


def update_data(request):
    # collection = Collection.objects.get(pk=11)
    # # collection.title = 'Game'
    # collection.featured_product = None
    # collection.save()
    collection = Collection.objects.filter(pk=11).update(featured_product=None)
    return render(request, 'update_data.html', {'collection': collection})


def delete_data(request):
    collection = Collection(pk=11)
    collection.delete()

    Collection.objects.filter(pk__gt=5).delete()

