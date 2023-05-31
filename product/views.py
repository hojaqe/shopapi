from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.permissions import IsAdminUser, AllowAny
from review.models import Like
from review.serializers import LikeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from review.serializers import FavoriteSerializer
from review.models import Favorite
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PermissionMixin:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser]
        else:
            permissions = [AllowAny]

        return [permission() for permission in permissions]



class CategoryViewSet(PermissionMixin,ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(PermissionMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['title', 'created_at']
    ordering_fields = ['title']


    @action(methods=['POST'], detail=True )
    def like(self, request, pk=None):
        product = self.get_object()
        author = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author=author)
                like.delete()
                message = 'disliked'
            except Like.DoesNotExist:
                Like.objects.create(product=product, author=author)
                message = 'liked'
            return Response(message, status=200)
    
    @action(methods=['POST'], detail=True )
    def favorite(self, request, pk=None):
        product = self.get_object()
        author = request.user
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                favorite = Favorite.objects.get(product=product, author=author)
                favorite.delete()
                message = 'deleted from favorits'
            except Favorite.DoesNotExist:
                Favorite.objects.create(product=product, author=author)
                message = 'Added to favorites'
            return Response(message, status=200)
            

            

