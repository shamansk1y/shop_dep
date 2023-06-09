from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.forms import ContactUsForm, SubscriptionForm
from main_page.models import Subscription, ContactUs
from orders.models import OrderItem, Order
from shop.models import Category, Product, Size, Manufacturer
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()


def handle_post_request(request):

    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')



def index(request):
    cart = Cart(request)

    if request.method == 'POST':
        handle_post_request(request)
    data = {
        'cart': cart,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'index.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'contact.html', context=data)


def category_list(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'category_list.html', context=data)


def sub_category_list(request, slug):
    cart = Cart(request)
    cat = get_object_or_404(Category, slug=slug)
    child = cat.children.all()

    # Обработка параметра сортировки
    sort_by = request.GET.get('sort', '')
    if sort_by == 'price_asc':
        cat_products = Product.objects.filter(category=cat).order_by('price')
    elif sort_by == 'price_desc':
        cat_products = Product.objects.filter(category=cat).order_by('-price')
    else:
        cat_products = Product.objects.filter(category=cat)
    manufacturer_filters = request.GET.getlist('manufacturer_filter')
    size_filters = request.GET.getlist('size_filter')

    price_ranges = [
        {'id': '1-500', 'name': 'від 1 до 500 UAH', 'min': 1, 'max': 500},
        {'id': '501-1000', 'name': 'від 501 UAH до 1000 UAH', 'min': 501, 'max': 1000},
        {'id': '1001-1500', 'name': 'від 1001 UAH до 1500 UAH', 'min': 1001, 'max': 1500},
        {'id': '1501-2000', 'name': 'від 1501 UAH до 2000 UAH', 'min': 1501, 'max': 2000},
        {'id': '2001-1999', 'name': 'від 2001 та вище', 'min': 2001, 'max': 19999},
    ]
    if manufacturer_filters:
        cat_products = cat_products.filter(manufacturer__id__in=manufacturer_filters)
    if size_filters:
        cat_products = cat_products.filter(sizes__id__in=size_filters).distinct()
    price_filters = request.GET.getlist('price_filter')
    if price_filters:
        price_query = Q()
        for price_filter in price_filters:
            min_price, max_price = price_filter.split('-')
            if max_price:
                price_query |= Q(price__gte=min_price, price__lte=max_price)
            else:
                price_query |= Q(price__gte=min_price)
        cat_products = cat_products.filter(price_query)

    sizes = Size.objects.filter(products__in=cat_products).distinct()
    manufacturers = Manufacturer.objects.filter(product__in=cat_products).distinct()

    paginator = Paginator(cat_products, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'cat': cat,
        'child': child,
        'cart': cart,
        'cat_products': cat_products,
        'page_obj': page_obj,
        'sort_by': sort_by,
        'manufacturers': manufacturers,
        'sizes': sizes,
        'manufacturer_filters': manufacturer_filters,
        'size_filters': size_filters,
        'price_filters': price_filters,
        'price_ranges': price_ranges,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    if cat.is_parent():
        return render(request, 'sub_category_list.html', context=data)
    else:
        return render(request, 'sub_category_product_list.html', context=data)


def search(request):
    query = request.GET.get('q')
    search_products = Product.objects.filter(name__icontains=query)
    data = {'search_products': search_products, 'query': query}
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'search.html', context=data)


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_manager(request, pk):
    Subscription.objects.filter(pk=pk).update(is_processed=True)
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    OrderItem.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:manager_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def manager_list(request):
    subscription_viev_manager = Subscription.objects.filter(is_processed=False)
    contact_us_viev_manager = ContactUs.objects.filter(is_processed=False)
    orders = Order.objects.all()

    data = {
        'subscription_viev_manager': subscription_viev_manager,
        'contact_us_viev_manager': contact_us_viev_manager,
        'orders': orders,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'manager.html', context=data)