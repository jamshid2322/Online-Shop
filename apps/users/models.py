from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.users.managers import CustomManager
import apps.products as apps_products

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_likes_count(self):
        return apps_products.models.Like.objects.filter(user_id=self.id, liked=True).count()
    
    def get_wishlist_count(self):
        return apps_products.models.CardItem.objects.filter(user_id=self.id).count()
    
 