from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_delete

from SysErp import settings


class Product(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=50)
    prix = models.IntegerField(default=400)
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return f'Product :  {self.name} || Price : {self.prix} '


class Order(models.Model):
    order_date = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              default='New')  # Status can be 'New', 'Validated', 'Prepared', 'Completed', 'Declined'
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.customer_name} '


"""class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    productd = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    def __str__(self) -> str:
        return f'{self.order.customer_name} ||  {self.product.name}  ||  {self.quantity}'"""


class Validate(models.Model):
    STATUS_CHOICES = [
        ('Valider', 'Valider'),
        ('Refuser', 'Refuser'),
        ('En Attend', 'En Attend'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    validator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='validated_orders', null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Valider'  # You can set a default status if needed
    )

    def get_status_display_name(self):
        for status_choice in self.STATUS_CHOICES:
            if status_choice[0] == self.status:
                return status_choice[1]
        return self.status

    def __str__(self):
        return f'{self.order.customer_name} ||  {self.order.products.name}  || {self.order.quantity} '


class Prepare(models.Model):
    order = models.OneToOneField(Validate, on_delete=models.CASCADE, limit_choices_to={'status': 'Valider'})
    preparer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='prepared_orders', null=True)

    def __str__(self):
        return self.order.order.customer_name


class InformeClient(models.Model):
    order = models.OneToOneField(Validate, on_delete=models.CASCADE, limit_choices_to={'status': 'Refuser'})
    date_informe = models.DateTimeField()
    raison = models.CharField(max_length=200)
    preparer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='informed_client', null=True)

    def __str__(self):
        return f'{self.order.order.customer_name}  ||  {self.order.order.products.name}  ||  raison : {self.raison}'


class Invoice(models.Model):
    Payment_CHOICES = [
        ('Paye', 'Paye'),
        ('Annuler', 'Annuler'),
        (' Pending', 'Pending'),
    ]
    order = models.OneToOneField(Prepare, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)  # Initialize the price with 0 initially
    invoice_date = models.DateTimeField(default=timezone.now)  # Add a default value for invoice date
    C = models.CharField(
        max_length=10,
        choices=Payment_CHOICES,
        default='pending'  # You can set a default status if needed
    )

    def save(self, *args, **kwargs):
        self.price = self.order.order.order.products.prix * self.order.order.order.quantity
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return (f'Client: {self.order.order.order.customer_name} || Product: {self.order.order.order.products.name} || '
                f'Quantity: {self.order.order.order.quantity} ||  Price : {self.price}  || Payment_status : {self.C}')


class ProductAvailability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product}  ||  {self.is_available}'


class Test(models.Model):
    order = models.ForeignKey(Validate, on_delete=models.CASCADE, limit_choices_to={'status': 'Valider'})


class Aprovisinenemt(models.Model):
    order = models.OneToOneField(Validate, on_delete=models.CASCADE, limit_choices_to={'status': 'En Attend'})
    preparer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    new_quantity = models.IntegerField()

    def __str__(self):
        return self.order.order.customer_name


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


