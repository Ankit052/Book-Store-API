# Generated by Django 4.0 on 2022-01-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_category_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]