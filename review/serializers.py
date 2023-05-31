from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Comment, Rating, Like, Favorite


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment
    

class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    class Meta:
        model = Rating
        fields = '__all__'
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                'Rating must be in range 1 - 6'
            )
        return rating
    
    # def validate_product(self, product):
    #     if self.Meta.model.objects.filter(product=product).exists():
    #         raise ValidationError(
    #             'Вы уже оставляли рэйтинг'
    #         )
    #     return product

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating

    

class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    product = ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        like = Like.objects.create(author=user, **validated_data)
        return like
    

class FavoriteSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    product = ReadOnlyField()
    class Meta:
        model = Favorite
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        favorite = Favorite.objects.create(author=user, **validated_data)
        return favorite