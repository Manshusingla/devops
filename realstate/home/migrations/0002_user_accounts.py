# Generated by Django 4.1.5 on 2023-04-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=100)),
                ('user_address', models.CharField(max_length=100)),
            ],
        ),
    ]
