from django.db import models

# Create your models here.
# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    primaryCategory = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200)
    detail_text = models.TextField(max_length=1000)
    product_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    price = models.FloatField()
    slug = models.SlugField()

    def __str__(self):
        return self.product_name