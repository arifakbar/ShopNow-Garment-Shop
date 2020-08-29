from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',Contact,name='contact'),
    path('login/',Login,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout/',Logout,name='logout'),
    path('cart/',Cart,name='cart'),
    path('delete-order/<int:Oid>/',DeleteOrder,name="deleteOrder")
]