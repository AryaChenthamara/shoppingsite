from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Contact,Registration,Product,Cart,Wishlist,Category,Adminuser,Order,Checkout
# Create your views here.
def index(request):
    template = loader.get_template('index.html')

    if 'cid' in request.GET:
        cid = request.GET["cid"]
        prods = Product.objects.filter(pro_cat=cid).values()
    else:
        prods = Product.objects.all().values()
    
    cats = Category.objects.all().values()

    prods2 = Product.objects.filter(pro_cat=35).values()

    context = {
        'categories':cats,
        'products':prods,
        'prods2':prods2,

    }

    return HttpResponse(template.render(context,request))
 

def about(request):
    template = loader.get_template('about.html')
    
    return HttpResponse(template.render({},request))



def contact(request):
    if request.method=='POST':
        contact_name= request.POST['contact_name']
        contact_email= request.POST['contact_email']
        contact_message= request.POST['contact_message']

        contact = Contact(contact_name=contact_name,contact_email=contact_email,contact_message=contact_message)

        contact.save()

    template = loader.get_template('contact.html')
    return HttpResponse(template.render({},request))

def registration(request):
    if 'userses' in request.session:
        return HttpResponseRedirect('dashboard')
    if request.method=='POST':
        reg_name=request.POST['reg_name']
        reg_email=request.POST['reg_email']    
        reg_phonenumber=request.POST['reg_phonenumber']        
        reg_userid=request.POST['reg_userid']        
        reg_password=request.POST['reg_password']   

        registration = Registration(reg_name=reg_name,reg_email=reg_email,reg_phonenumber=reg_phonenumber,reg_userid=reg_userid,reg_password=reg_password)  

        registration.save()
         
    template = loader.get_template('registration.html')
    return HttpResponse(template.render({},request))     

def login(request):
    if 'userses' in request.session:
        return HttpResponseRedirect('dashboard')
    if request.method=='POST':
        login_name=request.POST['login_name']
        login_password=request.POST['login_password']

        login=Registration.objects.filter(reg_userid=login_name,reg_password=login_password).values()

        if login:
            request.session['userses']=login_name
            return HttpResponseRedirect('dashboard')

    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))


def dashboard(request):
    if 'userses' not in request.session:
        return HttpResponseRedirect('login')
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render({},request))

def logout(request):
    del request.session['userses']
    return HttpResponseRedirect('login')


def adminlogin(request):
    if 'adminses' in request.session:
        return HttpResponseRedirect('admindashboard')
    if request.method=='POST':
        admin_username=request.POST['admin_username']
        admin_password=request.POST['admin_password']

        login=Adminuser.objects.filter(admin_username=admin_username,admin_password=admin_password).values()

        if login:
            request.session['adminses']=admin_username
            return HttpResponseRedirect('admindashboard')

    template = loader.get_template('adminlogin.html')
    return HttpResponse(template.render({},request))

def admindashboard(request):
    if 'adminses' not in request.session:
        return HttpResponseRedirect('adminlogin')
    template = loader.get_template('admindashboard.html')
    return HttpResponse(template.render({},request))

def adminlogout(request):
    del request.session['adminses']
    return HttpResponseRedirect('adminlogin')

def addproduct(request):
    if request.method=='POST':
        pro_name= request.POST['pro_name']
        pro_price= request.POST['pro_price']
        pro_img= request.FILES['pro_img'].name
        pro_cat= request.POST['pro_cat']
        product = Product(pro_name=pro_name,pro_img=pro_img,pro_price=pro_price,pro_cat=pro_cat)

        product.save()

        f=request.FILES['pro_img']
 
        with open('pages/static/uploads/'+f.name,'wb+')as destination:  
            for chunk in f.chunks():  
                destination.write(chunk) 

    template = loader.get_template('addproduct.html')
    cats = Category.objects.all().values()

    context ={
        'cats':cats,

    } 
    return HttpResponse(template.render(context,request))

def products(request):
    
    template = loader.get_template('products.html')
    if 'cid' in request.GET:
        cid = request.GET["cid"]
        prods = Product.objects.filter(pro_cat=cid).values()
    else:
        prods = Product.objects.all().values()
    
    cats = Category.objects.all().values()
    prods2 = Product.objects.filter(pro_cat=35).values()


    context = {
        'products':prods,
        'categories':cats,
        'prods2':prods2,

    }
    return HttpResponse(template.render(context,request))

def adminproducts(request):
    template = loader.get_template('adminproducts.html')
    products = Product.objects.all().values

    context = {
        'products':products,
    
    }
    return HttpResponse(template.render(context,request))



def editproduct(request,id):
    if request.method=='POST':
        pid= request.POST['id']
        pro_name= request.POST['pro_name']
        pro_price= request.POST['pro_price']
        pro_cat= request.POST['pro_cat']

        pro = Product.objects.filter(id=pid)[0]
        pro.pro_name=pro_name
        pro.pro_price=pro_price
        pro.pro_cat=int(pro_cat)

        if len(request.FILES) != 0:
            pro_img= request.FILES['pro_img']
            with open('pages/static/uploads/'+pro_img.name,'wb+')as destination:  
                for chunk in pro_img.chunks():  
                    destination.write(chunk) 

            pro.pro_img= pro_img.name

        pro.save()

    template = loader.get_template('editproduct.html')
    product = Product.objects.filter(id=id)[0]
    cats = Category.objects.all().values()

    context = {
        'product':product,
        'cats':cats,
        
    
    }
    return HttpResponse(template.render(context,request))


def addtocart(request,id):

    current_user = request.session['userses']
    #change quantity while adding same product again
    exist = Cart.objects.filter(pro_id=id,pro_user=current_user)

    def addQty():
        cart = Cart.objects.filter(pro_id=id,pro_user=current_user)[0]
        cart.pro_qty=cart.pro_qty+1
        cart.pro_tot=cart.pro_price*cart.pro_qty
        cart.save()

    if 'add' in request.GET:
        addQty()
        
    elif 'rem'in request.GET:
        cart = Cart.objects.filter(pro_id=id,pro_user=current_user)[0]
        if cart.pro_qty>1:
            cart.pro_qty=cart.pro_qty-1
            cart.pro_tot=cart.pro_price*cart.pro_qty
            cart.save()
    elif exist:
        addQty()
    else:
        prod = Product.objects.filter(id=id)[0]
        cart = Cart(pro_user=request.session['userses'],pro_id=prod.id,pro_name=prod.pro_name, pro_img=prod.pro_img, pro_price=prod.pro_price, pro_qty=1,pro_tot=prod.pro_price)
        cart.save()

    return HttpResponseRedirect("/cart")


def cart(request):
    if 'userses' not in request.session:
        return HttpResponseRedirect('login')
      
    current_user = request.session['userses']
    

    template = loader.get_template('cart.html')
    cart = Cart.objects.filter(pro_user=current_user).order_by("-id")

    gtot=0
    for x in cart:
        gtot+=x.pro_tot

    context = {
        'cart':cart,
        'gtot':gtot
    }
    return HttpResponse(template.render(context,request))



def checkout(request):
    cart = Cart.objects.all().order_by("-id")

    gtot=0
    for x in cart:
        gtot+=x.pro_tot

    context = {
        'cart':cart,
        'gtot':gtot
    }

    template = loader.get_template('checkout.html')
    return HttpResponse(template.render(context,request))



def order(request):
     if request.method=='POST':
        order_address=request.POST['order_address']
        order_landmark=request.POST['order_landmark']
        order_pincode=request.POST['order_pincode']   
        order_phone=request.POST['order_phone'] 
        pay_method=request.POST['pay_method']

        cart = Cart.objects.all()
        for x in cart:
            pro_user = x.pro_user
            pro_name= x.pro_name
            pro_price= x.pro_price
            pro_id=x.pro_id
            pro_img= x.pro_img
            pro_qty= x.pro_qty
            pro_tot= x.pro_tot
             
            order = Order(pro_user=pro_user,order_address=order_address,order_landmark=order_landmark,order_pincode=order_pincode,order_phone=order_phone,pay_method=pay_method,order_name=pro_name,order_img=pro_img,order_price=pro_price,pro_id=pro_id,order_qty=pro_qty,order_tot= pro_tot)

            order.save()

            x.delete()

        return HttpResponseRedirect("/order")
     current_user = request.session['userses']

     order = Order.objects.filter(pro_user=current_user,order_status=0)
     gtot=0
     for x in order:
        gtot+=x.order_tot

     for x in order:
        adrs1=x.order_address
        adrs2=x.order_landmark
        adrs3=str(x.order_pincode)
        adrs4=str(x.order_phone)
        adrs5=str(x.pay_method)

        break

     context = {
        'order':order,
        'gtot':gtot,
        'adrs':[adrs1,adrs2,adrs3,adrs4,adrs5],
    }
     template = loader.get_template('order.html')
     return HttpResponse(template.render(context,request))

def orderstatus(request):
    if request.method=='POST':
      
        pay_method=request.POST['pay_method']
        
        order = Order.objects.all()
        for x in order:
            pro_name= x.pro_name
            pro_price= x.pro_price
            pro_id=x.pro_id
            pro_img= x.pro_img
            pro_qty= x.pro_qty
            pro_tot= x.pro_tot
            pro_user= x.current_user
             
            order = Order(pro_user=pro_user,pay_method=pay_method,order_name=pro_name,order_img=pro_img,order_price=pro_price,pro_id=pro_id,order_qty=pro_qty,order_tot= pro_tot)

            order.save()



        return HttpResponseRedirect("/order")

    order = Order.objects.all().order_by("-id")
    count = Order.objects.all().count()
    gtot=0
    i=1
    for x in order:
        gtot+=x.order_tot

    context = {
        'order':order,
        'gtot':gtot,
        'count':count,
       
    }

    template = loader.get_template('orderstatus.html')
    return HttpResponse(template.render(context,request))

def myorders(request):
    if request.method=='POST':
      
        pay_method=request.POST['pay_method']
        
        order = Order.objects.all()
        for x in order:
            pro_name= x.pro_name
            pro_price= x.pro_price
            pro_id=x.pro_id
            pro_img= x.pro_img
            pro_qty= x.pro_qty
            pro_tot= x.pro_tot
             
            order = Order(pay_method=pay_method,order_name=pro_name,order_img=pro_img,order_price=pro_price,pro_id=pro_id,order_qty=pro_qty,order_tot= pro_tot)

            order.save()



        return HttpResponseRedirect("/order")

    order = Order.objects.all().order_by("-id")
    count = Order.objects.all().count()
    gtot=0
    i=1
    for x in order:
        gtot+=x.order_tot

    context = {
        'order':order,
        'gtot':gtot,
        'count':count,
       
    }

    template = loader.get_template('myorders.html')
    return HttpResponse(template.render(context,request))


def delorder(request,id):
    prod = Order.objects.filter(id=id)[0]
    prod.delete()

    return HttpResponseRedirect("/order")
def placeorder(request):
    if 'userses' not in request.session:
        return HttpResponseRedirect('login')
    current_user = request.session['userses']

    order = Order.objects.filter(pro_user=current_user,order_status=0)[0]
    order.order_status=1
    order.save()

    template = loader.get_template('placeorder.html')
    
    return HttpResponse(template.render({},request))

def delcart(request,id):
    prod = Cart.objects.filter(id=id)[0]
    prod.delete()

    return HttpResponseRedirect("/cart")

def addtowishlist(request,id):
    
    x = Product.objects.filter(id=id)[0]
    wishlist = Wishlist(pro_name=x.pro_name, pro_img=x.pro_img, pro_price=x.pro_price)
    wishlist.save()
    return HttpResponseRedirect("/wishlist")


def wishlist(request):
   if 'userses' not in request.session:
        return HttpResponseRedirect('login') 
   template = loader.get_template('wishlist.html')
   wishlist = Wishlist.objects.all().order_by("-id")
   context = {
        'wishlist':wishlist,
        
    }

   return HttpResponse(template.render(context,request))


def delcart(request,id):
    prod = Cart.objects.filter(id=id)[0]
    prod.delete()

    return HttpResponseRedirect("/cart")



def delwish(request,id):
    prod = Wishlist.objects.filter(id=id)[0]
    prod.delete()

    return HttpResponseRedirect("/wishlist")



def addcategory(request):
    if request.method=='POST':
        cat_name= request.POST['cat_name']
        cat_img= request.FILES['cat_img'].name
    


        cat = Category(cat_name=cat_name,cat_img=cat_img)

        cat.save()

        f=request.FILES['cat_img']
 
        with open('pages/static/uploads/'+f.name,'wb+')as destination:  
            for chunk in f.chunks():  
                destination.write(chunk) 

    template = loader.get_template('addcategory.html')
    return HttpResponse(template.render({},request))



def searchproduct(request):
    query=request.GET['query']

    mydata = Product.objects.filter(pro_name__contains=query).values()

    context={
        'search': mydata,
        
    }

    template = loader.get_template('searchproduct.html')
    return HttpResponse(template.render(context,request))
 

def myorder(request):
    if request.method=='POST':
      
        pay_method=request.POST['pay_method']
        
        cart = Cart.objects.all()
        for x in cart:
            pro_name= x.pro_name
            pro_price= x.pro_price
            pro_id=x.pro_id
            pro_img= x.pro_img
            pro_qty= x.pro_qty
            pro_tot= x.pro_tot
             
            order = Order(pay_method=pay_method,order_name=pro_name,order_img=pro_img,order_price=pro_price,pro_id=pro_id,order_qty=pro_qty,order_tot= pro_tot)

            order.save()

            x.delete()

        return HttpResponseRedirect("/order")

    order = Order.objects.all().order_by("-id")
    count = Order.objects.all().count()
    gtot=0
    i=1
    for x in order:
        gtot+=x.order_tot

    context = {
        'order':order,
        'gtot':gtot,
        'count':count,
       
    }

    template = loader.get_template('myorder.html')
    return HttpResponse(template.render(context,request))




 