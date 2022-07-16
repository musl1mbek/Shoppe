from ast import Is
import email
from itertools import product
from math import prod
from queue import LifoQueue
import re
from tkinter.messagebox import RETRY
from xml.etree.ElementTree import QName
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from datetime  import datetime
import datetime

# Api uchun funksiyalar

@api_view(['GET'])
def Get_Slider(request):
    a = Product.objects.filter(slider=True)
    ser = ProductSerializer(a,many = True)
    return Response(ser.data)

@api_view(['GET'])
def PriceFilter(r,start,finish):
    filterin = []
    a=Product.objects.all()
    for p in a:
        if start < p.price < finish:
            filterin.append(p)
        else:
            print('fskafkhakshfkahfk')
    ser = ProductSerializer(filterin,many=True)
    return Response(ser.data)


@api_view(['GET'])
def Get_Productlast6(request):
    a = Product.objects.all().order_by('-id')[:6]
    ser = ProductSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Get_Product(request):
    a = Product.objects.all()
    ser = ProductSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Get_CategoryProduct(request):
    a = CategoryProduct.objects.all()
    ser = CategoryProductSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def FlProductname(request):
    name = request.GET['search']
    a = Product.objects.filter(name__icontains=name)
    ser = ProductSerializer(a,many=True)
    return Response(ser.data)


@api_view(['GET'])
def blog(request,pk):
    a = Blog.objects.get(id=pk)
    ser = BlogSerializer(a)
    return Response(ser.data)

@api_view(["GET"])
def GetBlogTags(request):
    a =  Tags.objects.all()
    ser =  TagsSerializer(a, many=True)
    return Response(ser.data)




@api_view(['GET'])
def blog_detail(request):
    a = Blog.objects.all().order_by('-id')[:4]
    ser = BlogSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def GetBlog_Comments(request):
    a = Blog_Comments.objects.all()
    ser = Blog_CommentsSerializer(a,many=True)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateBlog_Comments(request,pk):
    web_site = request.POST.get('web_site')
    name = request.POST.get('name')
    email = request.POST.get('email')
    comment =request.POST.get('comment')
    blog = Blog.objects.get(id=pk)
    user = request.user
    Blog_Comments.objects.create(user=user,comment=comment,web_site=web_site,name=name,email=email,blog=blog)
    b = Blog_Comments.objects.all().order_by('-id')
    ser = Blog_CommentsSerializer(b,many=True)
    return Response(ser.data)





@api_view(['GET'])
def GetCookies(request):
    a = Cookies.objects.all().order_by('-id')[:2]
    ser = CookiesSerializer(a,many=True)

    return Response(ser.data)


@api_view(['GET'])
def GetPrivacy_Policy(request):
    a = Privacy_Policy.objects.last()
    ser = Privacy_PolicySerializer(a)

    return Response(ser.data)



@api_view(['GET'])
def GetAbout(request):
    a = About.objects.last()
    ser = AboutSerializer(a)

    return Response(ser.data)


@api_view(['GET'])
def GetCoupons(request):
    a = Coupons.objects.all()
    ser = CouponsSerializer(a,many=True)

    return Response(ser.data)

    

@api_view(['GET'])
def GetUsedcoupons(request):
    a = Usedcoupons.objects.all()
    ser = UsedcouponsSerializer(a,many=True)

    return Response(ser.data)

@api_view(['GET'])
def GetCountry(request):
    a = Country.objects.all()
    ser = CountrySerializer(a , many= True)

    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Wishlist_Funk(request,pk):
    user = request.user
    product = Product.objects.get(id=pk)
    wis = Wishlist.objects.filter(user=user, product=product)
    if len(wis) == 0:
        wishlist = Wishlist.objects.create(user=user, product=product)
        return Response({"click":True})
    else:
        wis[0].delete()
        return Response({"click":False})
    


@api_view(['GET'])
def Get_Oneproduct(r,pk):
    a = Product.objects.filter(id=pk)
    ser = ProductSerializer(a,many=True)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Create_Reviews(request,pk):
    reviews = request.POST.get('reviews')
    name = request.POST.get('name')
    email = request.POST.get('email')
    star = request.POST.get('star')
    product = Product.objects.get(id=pk)
    user = request.user
    Reviews.objects.create(user=user,product=product,reviews=reviews,name=name,email=email,star=star)
    b = Reviews.objects.all().order_by('-id')
    ser = ReviewsSerializer(b,many=True)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateCard(request,pk):
    user = request.user
    n = Product.objects.filter(id=pk)
    Card.objects.create(product=n,quantity=12,user=user)
    a = Card.objects.all()
    ser = CardSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Card_Delete(request,pk):
    user = request.user 
    a = Card.objects.get(id=pk)
    a.delete
    return Response({'delete':'delete'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def UpdateCart(request, pk):
    user = request.user
    new_quantity = request.POST.get('quantity')
    cart = Card.objects.get( user= user,  id=pk)
    cart.quantity = new_quantity
    cart.save()
    ser = CardSerializer(cart)

    return Response(ser.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def  GetNewLetteer(request):
    user = request.user
    email = request.POST.get('email')
    a =  NewLetteer.objects.create(user=user,email=email)
    ser =  NewLetteerSerializer(a)
    return Response(ser.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateContacUs(request):
    user = request.user
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = request.POST.get('subject')
    product= request.POST.get('product')
    product = Product.objects.get(id=product)
    a = ContactUs.objects.create(user=user,first_name=first_name, product=product,last_name=last_name,  subject=subject, message=message, email=email )
    ser = ContactUsSerializer(a)
    return Response(ser.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateAddress(request):
    user = request.user
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    company_name = request.POST.get('company_name')
    street_address = request.POST.get('street_address')
    postcode= request.POST.get('postcode')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    country= request.POST.get('country')
    country = Country.objects.get(id=country)
    a =  Address.objects.create(user=user,city =city , phone=phone,postcode=postcode,first_name=first_name, country=country,last_name=last_name,  street_address=street_address, company_name=company_name, email=email )
    ser =  AddressSerializer(a)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def GetAddress(request):
    user = request.user
    a = Address.objects.all()
    ser = AddressSerializer(a,many=True)

    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def UpdateAddress(request, pk):
    user = request.user
    new_first_name= request.POST.get('first_name')
    new_last_name = request.POST.get('last_name')
    new_email = request.POST.get('email')
    new_company_name = request.POST.get('company_name')
    new_street_address = request.POST.get('street_address')
    new_postcode = request.POST.get('postcode')
    new_city = request.POST.get('city')
    new_phone = request.POST.get('phone')
    new_country = request.POST.get('country')
    new_country = Country.objects.get(id=new_country)
    address = Address.objects.get( user= user,  id=pk)
    address.first_name = new_first_name
    address.last_name = new_last_name
    address.email = new_email
    address.company_namey = new_company_name 
    address.street_address = new_street_address
    address.postcode = new_postcode
    address.city = new_city
    address.phone = new_phone
    address.country = new_country
    address.save()
    ser = AddressSerializer(address)

    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateAccounts(request):
    user = request.user
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password ')
    display_name = request.POST.get('display_name')
    shippingAddress = request.POST.get('shippingAddress')
    shippingAddress = Shippingaddress.objects.get(id=shippingAddress)
    address= request.POST.get('address')
    a =  Address.objects.create(user=user,shippingAddress =shippingAddress ,address=address,password=password ,display_name=display_name,first_name=first_name, last_name=last_name,email=email )
    ser =  AddressSerializer(a)
    return Response(ser.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CreateShippingaddress(request):
    user = request.user
    postcode= request.POST.get('postcode')
    city = request.POST.get('city')
    country= request.POST.get('country')
    card = request.POST.get('card')
    card = Card.objects.get(id=card)
    country = Country.objects.get(id=country)
    a =  Address.objects.create(user=user,city =city ,postcode=postcode, country=country, email=email,card=card )
    ser =  AddressSerializer(a)
    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def  GetRestoreAccount(request):
    user = request.user
    email = request.POST.get('email')
    a =  RestoreAccount.objects.create(user=user,email=email)
    ser =  RestoreAccountSerializer(a)
    return Response(ser.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def OrdetCreate(request):
    user = request.user
    cart = Card.objects.filter(user=user)
    for c in cart:
        order = Order.objects.create(user=user, date=datetime.datetime.now(), totle_price = c.product.price*c.quantity,product=c.product)
        # order_item = OrderItem.objects.create(order=order, product=c.product, quantity=c.quantity)
        c.delete()
        
    orders = Order.objects.all().order_by('-id')[:100]
    ser = OrderItemSerializer(orders, many = True)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def GetOrder(request):
    user = request.user
    a = Order.objects.all()
    ser = OrderSerializer(a,many=True)

    return Response(ser.data)


# Admin panel uchun funksiyalar

# def Index(request):
#     context = {

        
#     }
#     return render(request, 'index.html',context)

# def Category_Product_Html(request):
#     context={
#         'category' : CategoryProduct.objects.all()
#     }
#     return render (request, 'CategoryProduct.html',context)

# def Colors_Product_Html(request):
#     context={
#         'category' : Colours.objects.all()
#     }
#     return render(request, 'Color_product.html',context)

# def Product_Html(request):
#     context={
#         'category' : Product.objects.all()
#     }
#     return render(request, 'Product.html',context)

# def DeleteProduct(request, pk):
#     todo = Product.objects.get(id=pk)
    
#     todo.delete()
#     return redirect('product')