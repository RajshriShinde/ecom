# Generated by Django 4.1.dev20211004082034 on 2021-10-30 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_category_subcategories_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.product'),
        ),
    ]
