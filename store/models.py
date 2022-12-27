from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    priceSell = models.FloatField()
    priceBuy = models.FloatField()

    def __str__(self):
        return self.name

    def create_discount(self, discount):
        return self.priceSell - (self.priceSell * discount) / 100

    def profit(self):
        profit = self.priceSell - self.priceBuy
        return (profit * 100) / self.priceBuy

class Image(models.Model):
    image = models.ImageField(upload_to="products_images")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
