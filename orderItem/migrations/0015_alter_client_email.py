# Generated by Django 5.0 on 2023-12-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0014_alter_client_options_alter_client_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
