from django.shortcuts import render
from .models import Product,Contact
from math import ceil
# Create your views here.
from django.http import HttpResponse

def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={ item['category'] for item in catprods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])

    params={'allprods':allprods}
    return render(request, 'shop/index.html',params)

def test(request):
    products=Product.objects.all()
    return render(request, 'shop/test.html',{'products':products})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if(request.method=="POST"):
        name= request.POST.get('name','')
        phone=request.POST.get('phone',"")
        email=request.POST.get('email',"")
        desc=request.POST.get('desc',"")
        contact=Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/productview.html',{"product":product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

