<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-08-12 05:21
=======
# Generated by Django 2.0.13 on 2020-08-12 06:59
>>>>>>> ed794afaa33737294075e69be89ebf368d07735b

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_point_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_point',
            name='tel',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
