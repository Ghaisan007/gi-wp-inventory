from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    base_atk = models.IntegerField(null=True)
    substat = models.CharField(max_length=255, null=True)
    weapon_passive = models.TextField(null=True)
    weapon_type = models.CharField(max_length=255, null=True)
    rarity = models.CharField(max_length=255, null=True)