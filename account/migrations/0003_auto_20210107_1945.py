# Generated by Django 3.1.3 on 2021-01-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
