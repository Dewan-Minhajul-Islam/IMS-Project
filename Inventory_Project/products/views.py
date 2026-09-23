from django.shortcuts import render
from products.models import ProductModel


# Create your views here.
def home_view(request):
    
    return render(request, 'home.html')


def product_view(request):
    
    pr_data = ProductModel.objects.all()
    
    context = {
        'p_data' : pr_data 
    }
    
    return render(request, 'all-product.html', context)


def product_form(request):
    
    return render(request, 'add-product.html')