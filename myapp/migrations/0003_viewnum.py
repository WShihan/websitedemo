# Generated by Django 3.0.6 on 2020-06-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_bookviewnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]