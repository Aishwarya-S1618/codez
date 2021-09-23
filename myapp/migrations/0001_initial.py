# Generated by Django 3.2.7 on 2021-09-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=10)),
                ('comment', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
