# Generated by Django 5.0 on 2023-12-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0012_client_password_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
