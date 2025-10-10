from django.shortcuts import render

# Create your views here.
def cart_detail(request):
    # Logic to display cart details
    return render(request, 'cart/cart_detail.html')

def add_to_cart(request, product_id):
    # Logic to add a product to the cart
    return render(request, 'cart/cart_detail.html')
def remove_from_cart(request, product_id):
    # Logic to remove a product from the cart
    return render(request, 'cart/cart_detail.html')