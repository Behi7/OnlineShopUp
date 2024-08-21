from rest_framework import serializers
from Goods import models
from django.contrib.auth import get_user_model

class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'img']


class ProducDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, *args, **kwargs):
        user = User.objects.create_user(*args, **kwargs)
        return user
    

class CartSerializers(serializers.ModelSerializer):
        class Meta:
            model = models.Cart
            fields = '__all__'


class CartProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Info
        fields = '__all__'


class WishSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'


class EnterProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'