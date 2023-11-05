# Generated by Django 4.1 on 2023-11-03 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=100)),
                ('status', models.CharField(default='New', max_length=20)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=50)),
                ('prix', models.IntegerField(default=400)),
                ('quantity_available', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Validate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Valider', 'Valider'), ('Refuser', 'Refuser'), ('En Attend', 'En Attend')], default='Valider', max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderItem.order')),
                ('validator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='validated_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(limit_choices_to={'status': 'Valider'}, on_delete=django.db.models.deletion.CASCADE, to='orderItem.validate')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderItem.product')),
            ],
        ),
        migrations.CreateModel(
            name='Prepare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(limit_choices_to={'status': 'Valider'}, on_delete=django.db.models.deletion.CASCADE, to='orderItem.validate')),
                ('preparer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prepared_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderItem.product'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderItem.order')),
            ],
        ),
        migrations.CreateModel(
            name='Aprovisinenemt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_quantity', models.IntegerField()),
                ('order', models.ForeignKey(limit_choices_to={'status': 'En Attend'}, on_delete=django.db.models.deletion.CASCADE, to='orderItem.validate')),
                ('preparer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]