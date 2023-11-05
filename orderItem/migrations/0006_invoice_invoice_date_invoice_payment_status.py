# Generated by Django 4.1 on 2023-11-04 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0005_alter_invoice_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]