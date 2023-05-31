from django.db import models
from slugify import slugify



class Category(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=120, unique=True, primary_key=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    title = models.CharField(max_length=120, unique=True, verbose_name='Название продукта')
    slug = models.SlugField(max_length=120, unique=True, blank=True, primary_key=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    in_stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
