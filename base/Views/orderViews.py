#checkout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from ..models import Profile,Category,Order,Product,OrderDetail
from rest_framework.response import Response
from ..serializers import categorySerializer,productSerializer,orderSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToOrders(request):
    # data=request.data
    # user=request.user
    # orderDetails=data['order_details']
    
    # order=Order.objects.create(
    #         user=user,
    #         total_price=int(i['total_price']),

    # )
    order= request.data
    user = request.user
    print(user)
    order_total=0
    for x in order:
        prod_total= x["total_price"]
        order_total= order_total + int(prod_total)
    # total_order= request.data[""]
    new_order_id= Order.objects.create(user_id=user, total=order_total)
    print(order)
    for x in order:
        print(x)
        prod_id=Product.objects.get(_id=x["_id"])
        prod_amount= x["amount"]
        prod_total= x["total_price"]
        # category_id=Category.objects.get(_id=x["category_id"])
        OrderDetail.objects.create(order_id=new_order_id,product_id=prod_id,amount= prod_amount, total=prod_total)

    return Response('order')


''' in progress '''
#checkout get

#order details get 