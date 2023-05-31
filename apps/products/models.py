# DJango modules
from django.db import models

# Internal modules
from apps.products.abstract_base import CustomAbstactBase
from apps.users.models import User


class Category(CustomAbstactBase):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


class Color(CustomAbstactBase):
    pass


class Product(CustomAbstactBase):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    discount = models.PositiveIntegerField(default=0)
    description = models.TextField()
    colors = models.ManyToManyField(Color)

    def get_one_image(self):
        return ProductImage.objects.filter(product_id=self.id).first().image
    
    def get_images(self):
        return ProductImage.objects.filter(product_id=self.id).all()
    
    def get_cardItem(self):
        return CardItem.objects.filter(product_id=self.id).all()


class StarToProduct(models.Model):
    STARS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    star = models.CharField(max_length=1, choices=STARS)
    created_at = models.DateTimeField(auto_now_add=True)
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.product.name
    


class CardItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.qty}"
    
    def totalprice(self):
        totalprice = self.product.price * self.qty
        return totalprice
    



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.user.phone_number} {self.liked}" 
    

class TotalCartPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
