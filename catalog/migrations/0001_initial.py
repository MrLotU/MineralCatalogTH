# Generated by Django 2.0.6 on 2018-06-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('caption', models.TextField()),
                ('img', models.CharField(max_length=255)),
                ('fields', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
