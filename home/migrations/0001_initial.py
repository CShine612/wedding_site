# Generated by Django 3.2.15 on 2022-09-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('attending', models.BooleanField(blank=True)),
                ('meal', models.CharField(default='None', max_length=50)),
                ('comments', models.CharField(default='None', max_length=500)),
                ('plus_one', models.BooleanField(default=False)),
                ('group', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
