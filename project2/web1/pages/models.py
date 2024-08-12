from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_name
    
class Registration(models.Model):
    reg_name = models.CharField(max_length=225)
    reg_email = models.EmailField(max_length=255)
    reg_phonenumber = models.CharField(max_length=255)
    reg_userid = models.CharField(max_length=255)
    reg_password = models.CharField(max_length=255)

    def __str__(self): 
        return self.reg_name 

class Adminuser(models.Model):
    admin_name = models.CharField(max_length=225)
    admin_username = models.CharField(max_length=225)
    admin_password = models.CharField(max_length=255)

    def __str__(self): 
        return self.admin_name   
    
    
class Product(models.Model):
    pro_name = models.CharField(max_length=255)
    pro_cat = models.IntegerField(null=True)
    pro_price = models.FloatField()
    pro_img = models.CharField(max_length=255)
    pro_stock = models.CharField(max_length=255,default=1)


    def __str__(self):
        return self.pro_name
    
# class Payment(models.Model):
#      payment_address = models.CharField(max_length=255)
#      payment_landmark = models.CharField(max_length=255)
#      payment_pincode = models.IntegerField(null=True)
#      payment_phone = models.IntegerField(null=True)
#      def __str__(self):
#         return self. payment_address        
    
class Checkout(models.Model):
     checkout_address = models.CharField(max_length=255)
     checkout_landmark = models.CharField(max_length=255)
     checkout_pincode = models.IntegerField(null=True)
     checkout_phone = models.IntegerField(null=True)
     pay_method = models.CharField(max_length=10,null=True)
     pro_user = models.CharField(max_length=255,null=True)


     def __str__(self):
        return self. checkout_address    

class Order(models.Model):
    order_address = models.CharField(max_length=255)
    order_landmark = models.CharField(max_length=255)
    order_pincode = models.IntegerField(null=True)
    pay_method = models.CharField(max_length=10,null=True)
    order_phone = models.IntegerField(null=True)
    pro_id = models.IntegerField(null=True)
    pro_user = models.CharField(max_length=255,null=True)
    order_name = models.CharField(max_length=255)
    order_price = models.FloatField(null=True)
    order_img = models.CharField(max_length=255)
    order_qty = models.IntegerField(null=True)
    order_tot = models.FloatField()
    order_status = models.IntegerField(default=0)

    def __str__(self):
        return self.order_name
    
class Cart(models.Model):
    pro_user = models.CharField(max_length=255,null=True)
    pro_id = models.IntegerField(null=True)
    pro_name = models.CharField(max_length=255)
    pro_price = models.FloatField()
    pro_img = models.CharField(max_length=255)
    pro_qty = models.IntegerField()
    pro_tot = models.FloatField()

    def __str__(self):
        return self.pro_name

class Wishlist(models.Model):
    pro_user = models.CharField(max_length=255,null=True)
    pro_name = models.CharField(max_length=255)
    pro_price = models.FloatField()
    pro_img = models.CharField(max_length=255)
    pro_stock = models.CharField(max_length=255)

    def __str__(self) :
        return self.pro_name
            
class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_img = models.CharField(max_length=255)


                
    def __str__(self):
        return self.cat_name