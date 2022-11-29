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
from django.contrib.auth import logout


''' Done '''
# token- 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['email'] = user.email
        # send params into the token
        # should export it in the Loginslicer
        return token


''' Done '''
# log in
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


''' Done '''
# admin/user register
@api_view(['POST'])
def register(request):
    isStaff = request.data["is_staff"]
    user = User.objects.create_user(
        email=request.data["email"],
        password=request.data["password"],
        is_staff=isStaff,
        username=request.data["username"],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'])
    Profile.objects.create(user=user, phone=str(request.data['phone']),
                           address=request.data['address'], gender=request.data['gender'])
    return HttpResponse('register')






# Logout
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logOut(request):
    logout(request)
    return Response("logged out")


''' in progress'''

#update user

#delete user
