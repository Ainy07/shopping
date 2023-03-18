from django.shortcuts import render
from django.views import View
from . models import *


def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')



class ProductView(View):
    def get(self , request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        laptop= Product.objects.filter(category='L')
        mobile = Product.objects.filter(category='M')
        beauryitem = Product.objects.filter(category='BI')
        electronicitem = Product.objects.filter(category='ELE')
        watch = Product.objects.filter(category='W')
        bag = Product.objects.filter(category='B')
        return render(request , 'app\home.html' , {
            'topwear':topwear,'mobile':mobile,'laptop':laptop,'bottomwear':bottomwear
            ,'bags':bag,'beautyproduct':beauryitem,'electronic':electronicitem
            ,'watch':watch,
        })
