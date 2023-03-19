from django.shortcuts import render
from django.views import View
from . models import *


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

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




class ProductDetailView(View):
    def get(self , request , pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app\productdetail.html', {'product':product})
    
    
    
    

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data=='Apple' or data== 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(category='L')
    elif data=='Asus' or data== 'Apple':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discounted_price__lt=75000)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discounted_price__gt=75000)
    return render(request, 'app/laptop.html',{'laptops':laptops})

def topwear(request, data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data=='zara' or data== 'Nike':
        topwears = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=700)
    elif data == 'above':
        topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=700)
    return render(request, 'app/topwear.html',{'topwears':topwears})


def bottomwear(request, data=None):
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data=='zara' or data== 'Nike':
        bottomwears = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=1000)
    elif data == 'above':
        bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=1000)
    return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears})    



def bueatyproduct(request, data=None):
    if data == None:
        bueatyproduct = Product.objects.filter(category='BI')
    elif data=='Lakme' or data== 'Maybelline':
        bueatyproduct = Product.objects.filter(category='BI').filter(brand=data)
    elif data == 'below':
        bueatyproduct = Product.objects.filter(category='BI').filter(discounted_price__lt=5000)
    elif data == 'above':
        bueatyproduct = Product.objects.filter(category='BI').filter(discounted_price__gt=5000)
    return render(request, 'app/bueatyitem.html',{'bueatyitem':bueatyproduct})

def electronicitem(request, data=None):
    if data == None:
        electronicitem = Product.objects.filter(category='ELE')
    elif data=='samsung' or data== 'boat':
        electronicitem = Product.objects.filter(category='ELE').filter(brand=data)
    elif data == 'below':
        electronicitem = Product.objects.filter(category='ELE').filter(discounted_price__lt=25000)
    elif data == 'above':
        electronicitem = Product.objects.filter(category='ELE').filter(discounted_price__gt=25000)
    return render(request, 'app/electronicitem.html',{'electronicitem':electronicitem})

def watch(request, data=None):
    if data == None:
        watch = Product.objects.filter(category='W')
    elif data=='boat' :
        watch = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'below':
        watch = Product.objects.filter(category='W').filter(discounted_price__lt=10000)
    elif data == 'above':
        watch = Product.objects.filter(category='W').filter(discounted_price__gt=10000)
    return render(request, 'app/watch.html',{'watch':watch})


def bags(request, data=None):
    if data == None:
        bags = Product.objects.filter(category='B')
    elif data=='Caprese' or data== 'Lavie':
        bags = Product.objects.filter(category='B').filter(brand=data)
    elif data == 'below':
        bags = Product.objects.filter(category='B').filter(discounted_price__lt=5000)
    elif data == 'above':
        bags = Product.objects.filter(category='B').filter(discounted_price__gt=5000)
    return render(request, 'app/bags.html',{'bags':bags})