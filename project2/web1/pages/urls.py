from django.urls import path
from.import views

urlpatterns=[
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('registration',views.registration, name="registration"),
    path('login',views.login, name="login"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('logout',views.logout, name="logout"),
    path('adminlogin',views.adminlogin, name="adminlogin"),
    path('admindashboard',views.admindashboard, name="admindashboard"),
    path('adminlogout',views.adminlogout, name="adminlogout"),
    path('addproduct',views.addproduct, name="addproduct"),
    path('adminproducts',views.adminproducts, name="adminproducts"),
    path('orderstatus',views.orderstatus, name="orderstatus"),
    path('editproduct/<int:id>',views.editproduct, name="editproduct"),
    path('products',views.products, name="products"),
    path('cart',views.cart, name="cart"),
    path('addtocart/<int:id>',views.addtocart, name="addtocart"),
    path('wishlist',views.wishlist, name="wishlist"),
    path('addtowishlist/<int:id>',views.addtowishlist, name="addtowishlist"),
    path('delcart/<int:id>',views.delcart, name="delcart"),
    path('delwish/<int:id>',views.delwish, name="delwish"),
    path('addcategory',views.addcategory, name="addcategory"),
    path('searchproduct',views.searchproduct, name="searchproduct"),
    path('checkout',views.checkout, name="checkout"),
    path('order',views.order, name="order"),
    path('myorders',views.myorders, name="myorders"),
    path('delorder/<int:id>',views.delorder, name="delorder"),
    path('placeorder',views.placeorder, name="placeorder"),



    



   








]