# Generated by Django 4.2.7 on 2023-12-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mylogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
            ],
        ),
    ]
