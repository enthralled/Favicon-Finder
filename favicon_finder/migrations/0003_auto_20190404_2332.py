# Generated by Django 2.1.1 on 2019-04-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favicon_finder', '0002_auto_20190117_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favicon',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
