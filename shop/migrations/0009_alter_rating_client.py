# Generated by Django 4.2.4 on 2024-01-19 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rating_item_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.client'),
        ),
    ]