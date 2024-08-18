from rest_framework import viewsets
from .serializers import ProductListSerializers, ProducDetailSerializers, CategoryListSerializers, UserSerializer, CartSerializers, CartProductSerializers
from Goods import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class ProductListViews(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductListSerializers


class ProducDetailViews(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProducDetailSerializers


class CategoryListViews(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryDetailViews(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategoryListSerializers



class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username = username, password = password)
    print(user)
    if user is not None:
        token_key, _ = Token.objects.get_or_create(user = user)
        context = {
            'success':True,
            'username':user.username,
            'key':token_key
        }
    else:
        context = {
            'success':False
        }
    return Response(context)

authentication_classes([TokenAuthentication])
permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def cartGet(request):
    user = request.user
    cart, _ = models.Cart.objects.get_or_create(author = user.id)
    ser_data = CartSerializers(cart).data
    return Response(ser_data)

@api_view(['POST'])
def add_to_cart(request):
        data = request.data
        product_id = data.get('product_id')
        product = models.Product.objects.get(id=product_id)
        user = request.user
        cart, created = models.Cart.objects.get_or_create(author=user)
        cart_product, created = models.CartProduct.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            cart_product.quantity += 1
            cart_product.save()

        serializer = CartProductSerializers(cart_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST', 'DELETE'])
def delete_to_cart(request):
        data = request.data
        product_id = data.get('product_id')
        product = models.Product.objects.get(id=product_id)
        user = request.user
        cart = models.Cart.objects.get(author=user)
        cart_product = models.CartProduct.objects.get(
            cart=cart,
            product=product
        ).delete
        serializer = CartProductSerializers(cart_product)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'status': 'logout'})
    

def register(request):
     username = request.data.get('username')
     password = request.data.get('password')
     User,object.create_user(
          username = username,
          password = password
     )
     return Response({'status':'success'})