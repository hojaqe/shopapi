from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product
from django.db.models import Avg


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price < 0 :
            raise ValidationError(
                'price must be > 0'
            )
        return price
    
    def to_representation(self, instance):
        representation =super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        representation['comments'] = [i.body for i in instance.comments.all()]
        representation['rating'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        return representation

    
