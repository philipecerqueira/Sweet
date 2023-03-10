from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    priceSell = models.FloatField()
    priceBuy = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def create_discount(self, discount):
        return self.priceSell - (self.priceSell * discount) / 100

    def profit(self):
        profit = self.priceSell - self.priceBuy
        return (profit * 100) / self.priceBuy

class Image(models.Model):
    image = models.ImageField(upload_to="products_images")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
