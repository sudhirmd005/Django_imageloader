# Generated by Django 3.1.7 on 2021-03-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageloader',
            name='photo',
            field=models.ImageField(upload_to='drive'),
        ),
    ]
