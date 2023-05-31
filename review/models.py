from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product


User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body



class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Автор')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.rating
    
    

class Like(models.Model):
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} liked by {self.author.email}'
    

class Favorite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')


    def __str__(self):
        return f'{self.product.title} -> {self.author.email}'
