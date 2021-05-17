# Generated by Django 3.2.2 on 2021-05-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_querry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='name', max_length=50)),
                ('user_email', models.EmailField(default='email', max_length=50)),
                ('user_number', models.CharField(default='0', max_length=20)),
                ('user_querry', models.CharField(default='querry', max_length=1000)),
            ],
        ),
    ]