from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from ..models import Profile,Category,Order,Product,OrderDetail
from rest_framework.response import Response
from ..serializers import categorySerializer,productSerializer,orderSerializer


''' Done '''
#add product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# only for admin
def add_product(request):
    Product.objects.create(
    description=request.data['description'],
    photo=request.data['photo'],
    price=str(request.data['price']),
    user=request.user,
    category=Category.objects.get(name=request.data['category'])
    )
    return HttpResponse('regiser')



''' Done '''
#dispaly products
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_products(request,id=0):
    if int(id)> 0 : 
        product= Product.objects.filter(_id=id)
    else:
        product=Product.objects.all()
    serializer=productSerializer.ProductSerializer(product, many=True)
    return Response (serializer.data)


''' in progress '''
#update product

#delete product

# product per category + id  