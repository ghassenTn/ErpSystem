# Generated by Django 4.1 on 2023-11-04 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepare',
            name='order',
            field=models.ForeignKey(limit_choices_to={'status': 'Valider'}, on_delete=django.db.models.deletion.CASCADE, to='orderItem.validate', unique=True),
        ),
    ]
