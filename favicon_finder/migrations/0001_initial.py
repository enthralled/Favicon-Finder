# Generated by Django 2.1.1 on 2019-01-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('fav_url', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
