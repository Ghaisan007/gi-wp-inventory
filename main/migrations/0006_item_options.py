# Generated by Django 4.2.5 on 2023-10-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='options',
            field=models.TextField(null=True),
        ),
    ]
