# Generated by Django 3.2 on 2022-02-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='グループ名')),
                ('twitterUsername', models.CharField(max_length=15, verbose_name='Twitter Username')),
                ('twitterId', models.CharField(max_length=20, null=True, verbose_name='Twitter ID')),
                ('twitterName', models.CharField(max_length=50, null=True, verbose_name='Twitter Name')),
                ('twitterDescription', models.TextField(null=True, verbose_name='Twitter Description')),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Idol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名前')),
                ('twitterUsername', models.CharField(max_length=15, verbose_name='Twitter Username')),
                ('twitterId', models.CharField(max_length=20, null=True, verbose_name='Twitter ID')),
                ('twitterName', models.CharField(max_length=50, null=True, verbose_name='Twitter Name')),
                ('twitterDescription', models.TextField(null=True, verbose_name='Twitter Description')),
                ('group', models.ManyToManyField(to='main.Group', verbose_name='グループ名')),
            ],
            options={
                'db_table': 'idol',
            },
        ),
    ]
