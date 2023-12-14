from django.contrib import admin
from .models import Product, Order, Validate, Prepare, ProductAvailability, Invoice, Aprovisinenemt, Test, InformeClient
import pandas as pd
from django.http import HttpResponse
from django.utils import timezone
import numpy as np
from .actions import export_to_excel ,export_invoice_to_excel

class OrderAdmin(admin.ModelAdmin):
    actions = [export_to_excel]
    list_display = ['customer_name','products','quantity','status']
    list_filter = ['customer_name','status']



class InvoiceAdmin(admin.ModelAdmin):
    actions = [export_invoice_to_excel]
    # Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Validate)
admin.site.register(Prepare)
admin.site.register(ProductAvailability)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Aprovisinenemt)
admin.site.register(Test)
admin.site.register(InformeClient)
# Register your models here.
###custom admin panel
admin.site.site_header = 'Erp System gestion des commande '
admin.site.site_title = ' Gestion des commande '
