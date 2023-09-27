from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    description = models.TextField(null=True)
    base_atk = models.IntegerField(null=True)
    substat = models.CharField(max_length=255, null=True)
    weapon_passive = models.TextField(null=True)
    weapon_type = models.CharField(max_length=255, null=True)
    rarity = models.CharField(max_length=255, null=True)