
from django.shortcuts import render
from apps.product.models import Product
from django.core.mail import send_mail
from apps.vendor.models import Vendor


def frontpage(request):
   
    newest_products= Product.objects.all()[0:8]
    veshje=Product.objects.filter(category__slug='veshje')[0:4]
    ikona=Product.objects.filter(category__slug='Ikona')[0:4]
    kostume=Product.objects.filter(category__slug='kostume-popullore')[0:4]
    instrumente=Product.objects.filter(category__slug='instrumente-muzikore')[0:4]
    objekte=Product.objects.filter(category__slug='objekte-shtepie')[0:4]
    suvenire=Product.objects.filter(category__slug='suvenire')[0:4]
    punime=Product.objects.filter(category__slug='punime')[0:4]
    bizhuteri=Product.objects.filter(category__slug='bizhuteri-artizanale')[0:4]
    piktura=Product.objects.filter(category__slug='piktura')[0:4]
    shporta=Product.objects.filter(category__slug='shporta-me-thurrje')[0:4]

    vendors=Vendor.objects.all()[0:3]
    return render(request,'core/frontpage.html', {'newest_products':newest_products,
                    'veshje':veshje,'ikona':ikona, 'kostume':kostume,
                    'instrumente':instrumente, 'objekte':objekte,
                    'suvenire':suvenire,'punime':punime,
                    'bizhuteri':bizhuteri, 'piktura':piktura,
                    'shporta':shporta,
                    'vendors':vendors})


def contact(request):

    if request.method=='POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_text = request.POST['message_text']


        #send an email
        send_mail(
          'derguar nga ' + message_name ,
           message_text , 
           message_email ,
           ['eriseldashehaj@gmail.com'],
        )

        return render(request,'core/contact.html', {'message_name':message_name})


    else:
        return render(request,'core/contact.html')

def about_project(request):
    return render(request, 'core/about_project.html')


def error_404_view(request, exception):
    return render(request, 'core/404.html')
