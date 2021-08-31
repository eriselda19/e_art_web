
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify

from django.shortcuts import get_object_or_404, render, redirect

from .models import Vendor
from apps.product.models import Product
from apps.vendor.models import Vendor
from .forms import ProductForm



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('vendor_admin')
        else:
            messages.info(request,'Kredenciale te gabuara!')
            return redirect('login')


    else:
        return render(request, 'vendor/login.html')



#If the method of requesting is post then take the info of this post to create the form
#if the form is valid save the form info to the user
#Afer login we create the vendor with the user info

def become_vendor(request):
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
     
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Emri i perdoruesit ekziston')
                return redirect('become_vendor')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Emaili ekziston')
                return redirect('become_vendor')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                login(request,user)
                vendor=Vendor.objects.create(name=user.first_name, created_by=user)

        else:
            messages.info(request,'Fjalekalimet nuk perputhen')
            return redirect('become_vendor')
        
        return redirect('become_vendor')
    else:

        return render(request, 'vendor/become_vendor.html')



#this decorator before going to admin page checks if the vendor is logged in and then redirects 
#if not it redirects to the login page
#when returning the template of vendor we return also the vendor object that we got as input
@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    orders=vendor.orders.all()

    for order in orders:
        order.vendor_amount=0
        order.vendor_paid_amount=0
        order.fully_paid=True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount +=item.get_total_price()
                    order.fully_paid=False

    return render(request, 'vendor/vendor_admin.html ', {'vendor':vendor, 'products':products, 'orders':orders})


@login_required
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES)

        if form.is_valid():
            #commit false because we havent set the vendor
            product=form.save(commit=False)
            product.vendor=request.user.vendor
            product.slug=slugify(product.title)
            product.save()


            return redirect('vendor_admin')

    else:
        form=ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})


#editojme produktin duke marre requestin dhe primary key
#marrim te dhenat e vendor nga request dhe produktin specifik nepermjet pk
#formes se produktit i japim Post, files dhe instancen e produktit

@login_required
def edit_product(request, pk):
    vendor=request.user.vendor
    product=vendor.products.get(pk=pk)

    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES, instance=product)
    
        if form.is_valid():
            form.save()

            return redirect('vendor_admin')

    else:
        form=ProductForm(instance=product)
      
    return render(request, 'vendor/edit_product.html', {'form': form,  'product':product})





@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method=='POST':
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')

        if name:
            vendor.created_by.email=email
            vendor.created_by.save()

            vendor.name=name
            vendor.save()

            return redirect('vendor_admin')


    return render(request,'vendor/edit_vendor.html', {'vendor': vendor})


def vendors(request):
    vendors= Vendor.objects.all()
    return render(request,'vendor/vendors.html', {'vendors':vendors})


def vendor(request, vendor_id):
    vendor=get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vendor/vendor.html', {'vendor':vendor})


def logout(request):
    auth.logout(request)
    return redirect('frontpage')