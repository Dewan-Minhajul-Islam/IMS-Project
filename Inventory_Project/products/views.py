from django.shortcuts import render

# Create your views here.
def home_view(request):
    
    return render(request, 'home.html')


def product_view(request):
    
    return render(request, 'all-product.html')


def product_form(request):
    
    return render(request, 'add-product.html')