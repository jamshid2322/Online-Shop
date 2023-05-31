
from django.db import models

class CustomAbstactBase(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True
