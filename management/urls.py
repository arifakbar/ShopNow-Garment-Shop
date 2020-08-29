from django.urls import path
from .views import *

urlpatterns = [
    path('shop/<int:productId>/',Shop,name='shop'),
    path('about/',About,name='about'),
    path('mens/',Mens_All,name='mens'),
    path('womens/',Womens_All,name='womens'),
    path('kids/',Kids_All,name='kids'),
    path("mens_shirt/",Mens_Shirt,name='mens_shirt'),
    path("mens_tshirt/",Mens_Tshirt,name='mens_tshirt'),
    path("mens_jeans/",Mens_Jeans,name='mens_jeans'),
    path("mens_kurta/",Mens_Kurta,name='mens_kurta'),
    path("mens_blazer/",Mens_Blazer,name='mens_blazer'),
    path("womens_tops/",Womens_Top,name='womens_tops'),
    path("womens_dresses/",Womens_Dresses,name='womens_dresses'),
    path("womens_jeans/",Womens_Jeans,name='womens_jeans'),
    path("womens_saree/",Womens_Saree,name='womens_saree'),
    path("womens_westernwear/",Womens_Westernwear,name='womens_westernwear'),
    path("kids_boys/",Kids_Boys,name="kids_boys"),
    path("kids_girls/",Kids_Girls,name="kids_girls"),
    path("kids_infants/",Kids_Infants,name="kids_infants"),
    path('adminhome/',AdminHome,name="adminhome"),
    path('editproduct/',EditProducts,name='editproduct'),
    path('addproduct/',AddProducts,name='addproduct'),
    path('contactUs/',ContactMsg,name='contactus'),
]