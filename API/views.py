from rest_framework import viewsets
from .serializers import ProductListSerializers, ProducDetailSerializers, CategoryListSerializers, UserSerializer
from Goods import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token



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


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(user)