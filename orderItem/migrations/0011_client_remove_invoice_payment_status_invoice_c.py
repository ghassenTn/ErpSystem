# Generated by Django 5.0 on 2023-12-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0010_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='invoice',
            name='C',
            field=models.CharField(choices=[('Paye', 'Paye'), ('Annuler', 'Annuler'), (' Pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
