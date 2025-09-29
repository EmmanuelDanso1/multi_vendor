from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source="vendor.username", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "image",
            "vendor_name",
            "created_at",
        ]
