from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group
from .models import Menu, Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','groups']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'