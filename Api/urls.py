from importlib.abc import PathEntryFinder
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('get-slider/',Get_Slider),
    path('get_productlast6/',Get_Productlast6),
    path('CreateAccounts/',CreateAccounts),
    path('filter-price/<int:start>-<int:finish>/',PriceFilter),
    path('get-product/', Get_Product),
    path('create-wish-list/<int:pk>',Wishlist_Funk),
    path('one-product/',Get_Oneproduct),
    path('create_reviews/<int:pk>', Create_Reviews),
    path('blog/<int:pk>/',blog),
    path('blog-detail/',blog_detail),
    path('privacy_policy/',Privacy_Policy),
    path('getcookies/',Cookies),
    path('get_about/', About),
    path('get_coupons/',Coupons),
    path('createcontacus', CreateContacUs),
    path('getNewLetteer', GetNewLetteer),
    path('order/',OrdetCreate),
    path('createshippingaddress/',CreateShippingaddress),
    path('getrestoreaccount/',  GetRestoreAccount),
    path('getblogtags/', GetBlogTags),
    path('CreateBlog_Comments/', CreateBlog_Comments),
    path('GetOrder/',GetOrder),
]   