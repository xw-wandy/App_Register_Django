# Generated by Django 4.1.3 on 2022-11-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_login_data_cache'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_user', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Extends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contry', models.CharField(max_length=50)),
            ],
        ),
    ]
