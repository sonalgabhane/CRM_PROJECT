from rest_framework import serializers
from .models import Lead, customer, supplier, Sightseeing, Package, Hotel, Vehicle, User

class LeadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class SupplierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = supplier
        fields = '__all__'

class SightseeingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sightseeing
        fields = '__all__'

class PackageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class HotelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'