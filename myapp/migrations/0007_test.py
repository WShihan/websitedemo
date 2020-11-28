# Generated by Django 3.0.6 on 2020-10-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=15, unique=True)),
                ('pack_size', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=50)),
            ],
        ),
    ]
