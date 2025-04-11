
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from django.db.models import Sum  # Added this import

def home(request):
    # Get the search query from the request (if any)
    search_query = request.GET.get('q', '')  # 'q' is the name of the search input
    if search_query:
        # Filter products where the name contains the search query (case-insensitive)
        products = Product.objects.filter(name__icontains=search_query)
    else:
        # If no search query, show all products
        products = Product.objects.all()
    
    return render(request, 'marketplace/home.html', {'products': products, 'search_query': search_query})
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'marketplace/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.create(user=request.user, product=product)
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = cart_items.aggregate(total=Sum('product__price'))['total'] or 0
    return render(request, 'marketplace/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Placeholder logic for order placement
    return render(request, 'marketplace/orderconfirmation.html', {'product': product})

@login_required
def place_order_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items.exists():
        cart_items.delete()  # Clear cart after order
    return render(request, 'marketplace/orderconfirmation.html', {'message': 'Order placed successfully!'})