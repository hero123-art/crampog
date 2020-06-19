# Generated by Django 3.0.6 on 2020-05-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=100)),
                ('desc1', models.CharField(max_length=100)),
                ('desc2', models.CharField(max_length=100)),
                ('desc3', models.CharField(max_length=100)),
                ('desc4', models.CharField(max_length=100)),
                ('desc5', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]
