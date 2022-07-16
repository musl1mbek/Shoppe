from rest_framework import serializers
from .models import *

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = '__all__'



class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'




class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'




class NewLetteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLetteer
        fields = '__all__'




class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'




class ShippingaddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippingaddress
        fields = '__all__'




class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'




class RestoreAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestoreAccount
        fields = '__all__'




class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'




class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'




class Blog_CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Comments
        fields = '__all__'




class CookiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookies
        fields = '__all__'




class CookiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookies
        fields = '__all__'





class Privacy_PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy_Policy
        fields = '__all__'



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'



class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'



class UsedcouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usedcoupons
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = Order
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'