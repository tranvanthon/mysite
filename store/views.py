from django.shortcuts import render

# Create your views here.
def home(request):
    # Logic to display the home page
    return render(request, 'store/home.html')

def product_list(request):
    # Logic to display a list of products
    return render(request, 'store/product_list.html')

def product_detail(request, pk):
    # Logic to display product details
    return render(request, 'store/product_detail.html')
