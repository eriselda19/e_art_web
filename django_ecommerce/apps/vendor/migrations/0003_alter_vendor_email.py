# Generated by Django 3.2.5 on 2021-07-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
