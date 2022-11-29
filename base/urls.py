
from django.contrib import admin
from django.urls import path
from .Views import categoryViews,productViews,orderViews,authenticationViews

urlpatterns = [
 
    path('login/',authenticationViews.MyTokenObtainPairView.as_view(), name='login'), #works
    
    path('register/', authenticationViews.register, name="register"), #works

    path('addcategory/', categoryViews.add_category, name="addcategory"),#works

    path('getcategory/', categoryViews.get_category, name="getcategory"), #works

    path('getcategory/<id>', categoryViews.get_category, name="getcategory"), #works

    path('addproduct/', productViews.add_product, name="addproduct"), #works

    path('getproduct/', productViews.get_products, name="getproduct"), #works

    path('getproduct/<id>', productViews.get_products, name="getproduct"), #works

    path('checkout/', orderViews.addToOrders, name="checkout"), #

    


]
