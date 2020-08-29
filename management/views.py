from django.shortcuts import render,redirect
from .models import *
from customer.models import *
import itertools
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.

def About(request):
    return render(request,'about.html')
    
def Mens_All(request):
    mensLA = Products.objects.filter(category__startswith="Men",latestArrival=True)
    mensBS = Products.objects.filter(category__startswith="Men",bestSeller=True)
    d = {'mensLA':mensLA,'mensBS':mensBS}
    return render(request,'mens_all.html',d)

def Mens_Shirt(request):
    mensShirt = Products.objects.filter(category="Mens-Shirt")
    d = {'mensShirt':mensShirt}
    return render(request,'mens_shirt.html',d)    

    
def Mens_Tshirt(request):
    mensTshirt = Products.objects.filter(category="Mens-Tshirt")
    d = {'mensTshirt':mensTshirt}
    return render(request,'mens_tshirt.html',d)  

def Mens_Jeans(request):
    mensJeans = Products.objects.filter(category="Mens-Jeans")
    d = {'mensJeans':mensJeans}
    return render(request,'mens_jeans.html',d)  


def Mens_Kurta(request):
    mensKurta = Products.objects.filter(category="Mens-Kurta")
    d = {'mensKurta':mensKurta}
    return render(request,'mens_kurta.html',d)  

def Mens_Blazer(request):
    mensBlazer = Products.objects.filter(category="Mens-Blazer")
    d = {'mensBlazer':mensBlazer}
    return render(request,'mens_blazer.html',d)

def Womens_All(request):
    womensLA = Products.objects.filter(category__startswith="Women",latestArrival=True)
    womensBS = Products.objects.filter(category__startswith="Women",bestSeller=True)
    d = {'womensLA':womensLA,'womensBS':womensBS}
    return render(request,'womens_all.html',d)

def Womens_Top(request):
    womensTop = Products.objects.filter(category="Womens-Top")
    d = {'womensTop':womensTop}
    return render(request,'womens_tops.html',d)    
    
def Womens_Dresses(request):
    womensdresses = Products.objects.filter(category="Womens-Dresses")
    d = {'womensdresses':womensdresses}
    return render(request,'womens_dresses.html',d)  

def Womens_Jeans(request):
    womensJeans = Products.objects.filter(category="Womens-Jeans")
    d = {'womensJeans':womensJeans}
    return render(request,'womens_jeans.html',d)  

def Womens_Saree(request):
    womensSaree = Products.objects.filter(category="Womens-Saree")
    d = {'womensSaree':womensSaree}
    return render(request,'womens_saree.html',d)  

def Womens_Westernwear(request):
    womensWesternwear = Products.objects.filter(category="Womens-Western wear")
    d = {'womensWesternwear':womensWesternwear}
    return render(request,'womens_ww.html',d)

def Kids_All(request):
    kidsLA = Products.objects.filter(category__startswith="Kid",latestArrival=True)
    kidsBS = Products.objects.filter(category__startswith="Kid",bestSeller=True)
    d = {'kidsLA':kidsLA,'kidsBS':kidsBS}
    return render(request,'kids_all.html',d)  

def Kids_Boys(request):
    kidsBoys = Products.objects.filter(category="Kids-Boys")
    d = {'kidsBoys':kidsBoys}
    return render(request,'kids_boys.html',d)  

def Kids_Girls(request):
    kidsGirls = Products.objects.filter(category="Kids-Girls")
    d = {'kidsGirls':kidsGirls}
    return render(request,'kids_girls.html',d)  

def Kids_Infants(request):
    kidsInfants = Products.objects.filter(category="Kids-Infants")
    d = {'kidsInfants':kidsInfants}
    return render(request,'kids_infant.html',d)

def Shop(request,productId):
    product = Products.objects.filter(id=productId).first()
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        qty = request.POST['qty']
        data = Add_To_Cart.objects.filter(user=request.user,cloth=product).first()
        if data:
              Add_To_Cart.objects.filter(user=request.user,cloth=product).update(quantity=qty)
        else:
            Add_To_Cart.objects.create(user=request.user,cloth=product,quantity=qty)        
    d = {'product':product}
    return render(request,'shop.html',d)

def Cart(request):
    return render(request,'cart.html')

def AdminHome(request):
    if request.user.is_anonymous:
        return redirect ('login')
    if not request.user.is_staff:
        return redirect('home')
    orders = Add_To_Cart.objects.all()
    if 'confirmOrder' in request.POST:
        Add_To_Cart.objects.filter(id = request.POST['confirmOrder']).update(confirmation=True)
        r = Add_To_Cart.objects.get(id=request.POST['confirmOrder'])
        sub = "Order confirmed at ShopNow"
        from_mail = settings.EMAIL_HOST_USER
        data = {'name':r.user.username,'product':r.cloth.title,'quantity':r.quantity}
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub,'',from_mail,[r.user.email])
        msg.attach_alternative(html,'text/html')
        print('result = ', msg.send())
    if 'cancelOrder' in request.POST:
        Add_To_Cart.objects.filter(id = request.POST['cancelOrder']).update(confirmation=False)
        r = Add_To_Cart.objects.get(id=request.POST['cancelOrder'])
        sub = "Order canceled at ShopNow"
        from_mail = settings.EMAIL_HOST_USER
        data = {'name':r.user.username,'product':r.cloth.title,'quantity':r.quantity}
        html = get_template('mailCancel.html').render(data)
        msg = EmailMultiAlternatives(sub,'',from_mail,[r.user.email])
        msg.attach_alternative(html,'text/html')
        print('result = ', msg.send())          
    if 'deleteOrder' in request.POST:
        Add_To_Cart.objects.filter(id = request.POST['deleteOrder']).delete()          
    d={'orders':orders}        
    return render(request,'layout2.html',d)

def EditProducts(request):
    products = Products.objects.all()
    if 'notAvialable' in request.POST:
        Products.objects.filter(id=request.POST['notAvialable']).update(availability=False)
    if 'avialable' in request.POST:
        Products.objects.filter(id=request.POST['avialable']).update(availability=True)    
    d={'products':products}
    if 'removeLa' in request.POST:
        Products.objects.filter(id=request.POST['removeLa']).update(latestArrival=False)
    if 'addLa' in request.POST:
        Products.objects.filter(id=request.POST['addLa']).update(latestArrival=True)    
    d={'products':products}
    if 'removeBs' in request.POST:
        Products.objects.filter(id=request.POST['removeBs']).update(bestSeller=False)
    if 'addBs' in request.POST:
        Products.objects.filter(id=request.POST['addBs']).update(bestSeller=True)  
    if 'delete' in request.POST:
        Products.objects.filter(id = request.POST['delete']).delete()  
    d={'products':products}
    return render(request,'editproduct.html',d)   

def AddProducts(request):
    cat = list(map(list,Given_categories))  
    if request.POST:
        category = request.POST['category']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        stars = request.POST['stars']
        img = request.FILES['img'] 
        img1 = request.FILES['img1'] 
        img2 = request.FILES['img2'] 
        Products.objects.create(category=category,title=title,description=description,price=price,stars=stars,Image=img,Image1=img1,Image2=img2)
    d={'cat':cat}
    return render(request,'addproducts.html',d)

def ContactMsg(request):
    contactmsg = ContactUs.objects.all()
    d = {'contactmsg':contactmsg}
    if 'delete' in request.POST:
        ContactUs.objects.get(id = request.POST['delete']).delete()   
    return render(request,'contactUs.html',d) 
    

