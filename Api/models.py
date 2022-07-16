
from itertools import product
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Product uchun
# Productni Categoriyalari turishi uchun mdel
class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
# Productni ranglari uchun model


class Colours(models.Model):
    name = models.CharField(max_length=255)

# Product malumotlarini olish uchun model
class Product(models.Model):
    img = models.ImageField(upload_to = 'Product/')
    img2 = models.ImageField(upload_to = 'Product/',blank = True,null = True)
    img3 = models.ImageField(upload_to = 'Product/',blank = True,null = True)
    img4 = models.ImageField(upload_to = 'Product/',blank = True,null = True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    CategoryProduct = models.ManyToManyField(CategoryProduct)
    sku = models.IntegerField()
    description = models.TextField()
    weight = models.FloatField()
    dimentions = models.CharField(max_length=255)
    colours = models.ManyToManyField(Colours)
    material = models.CharField(max_length=255)
    # Product sliderda korinishi uchun field
    slider = models.BooleanField(default=False)

    
# Foydalanuvchiga yoqgan productni belgilash uchun
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# productni baholash uchun model
class Reviews(models.Model):
    reviews = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    star = models.IntegerField(choices=(
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5'),
    ), default=0)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)

# Foydalanuvchi yangilikarda habardor bolish uchun model 
class NewLetteer(models.Model):
    email = models.EmailField()

# Companiyaga foydalanuvchilar fikri haqida malumot berish uchun model
class ContactUs(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.CharField(max_length=400)









#  Foydalanuvchilar malumotini olish uchun modellar toplami
# Foydalanuvchi qaysi davlatdan ekanligini olish uchun model
class Country(models.Model):
    name = models.CharField(max_length=255)

# Foydalanuvchi manzili olish uchun model
class Address(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    postcode = models.IntegerField()
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

# foydalanuvchini oken orqali pochtani olishi uchun manzil kiritish modeli
class Shippingaddress(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postcode = models.IntegerField()
    city = models.CharField(max_length=255)

# Foydalanuvchi shaxsiy malumotlari turuvchi model
class Accounts(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=8)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shippingAddress = models.ForeignKey(Shippingaddress, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)   
    display_name = models.CharField(max_length=255) 

# akkauntioni qayta tiklash uchun emailini kiritish uchun model
class RestoreAccount(models.Model):
    email = models.EmailField()






# Blog page uchun modellar
# Blogdagi modellar uchun Categoriyalar
class Tags(models.Model):
    name = models.CharField(max_length=255)

# Blogdagi obyektlar uchun model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='Blog/')
    text = models.TextField()
    img2 = models.ImageField(upload_to='Blog/')
    title2 = models.TextField()
    Tags = models.ManyToManyField(Tags)

# Blog obyekti uchun kommentlar modeli
class Blog_Comments(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    web_site = models.URLField()
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)









# Privacy Policy page uchun
# sayt qoidalarini ozida jamlash
class Cookies(models.Model):
    cookies = models.CharField(max_length=255)

# Sayt hafsizligi qisqacha 
class Privacy_Policy(models.Model):
    title = models.TextField()
    security = models.TextField()
    coookies = models.ManyToManyField(Cookies)








# Aboaut page uchun modellar 
# sayt haqiad tushuncha berish uchun
class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='About/')
    text2 = models.CharField(max_length=255)
    image = models.ImageField()
    text3 = models.CharField(max_length=255)





# Cuponlar uchun model 
# Real vaqtda ishlanayotgan kuponlarni ozida jamlash
class Coupons(models.Model):
    name = models.CharField(max_length=255)



# Ishlatilingan kuponlarni ozida jamlash uchun
class Usedcoupons(models.Model):
    name = models.CharField(max_length=255)

class Card(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Order uchun modellar
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    totle_price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class OrderItem(models.Model):
    order  = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_system = models.CharField(max_length=255)