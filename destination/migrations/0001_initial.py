# Generated by Django 3.0.6 on 2020-05-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('point1', models.CharField(max_length=100)),
                ('point2', models.CharField(max_length=100)),
                ('point3', models.CharField(max_length=100)),
                ('point4', models.CharField(max_length=100)),
                ('point5', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]
