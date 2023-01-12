from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    temp_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "picture",
            "active",
            "temp_price"
        )
        
    def get_temp_price(self, obj):    
        return obj.price * 1.2