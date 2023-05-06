from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products': products})

def about(request):
    return HttpResponse('<h1> About me</h1>')

def contact(request):
    return HttpResponse('<h1> Contact Page </h1> ')