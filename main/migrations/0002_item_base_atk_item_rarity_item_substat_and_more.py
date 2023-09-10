# Generated by Django 4.2.5 on 2023-09-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='base_atk',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='rarity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='substat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weapon_passive',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weapon_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]