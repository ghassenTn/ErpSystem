from django.contrib import admin
from .models import Product, Order, Validate, Prepare, ProductAvailability, Invoice, Aprovisinenemt, Test, InformeClient
import pandas as pd
from django.http import HttpResponse
from django.utils import timezone


def export_to_excel(modeladmin, request, queryset):
    # Create a DataFrame from the selected orders
    data = {
        'Customer Name': [order.customer_name for order in queryset],
        'Product Name': [order.products.name for order in queryset],
        'Quantity': [order.quantity for order in queryset],
        'Order Date': [order.order_date.astimezone(timezone.utc).replace(tzinfo=None) for order in queryset],
        'Status': [order.status for order in queryset],
    }
    df = pd.DataFrame(data)

    # Create an Excel writer using pandas
    writer = pd.ExcelWriter('selected_orders.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Orders', index=False)

    # Close the Pandas Excel writer
    writer.save()

    # Generate an HTTP response to serve the Excel file for download
    with open('selected_orders.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="selected_orders.xlsx"'

    return response


export_to_excel.short_description = "Export  orders to Excel"


def msg(modeladmin, request, queryset):
    return HttpResponse(f"<script>alert('{[Order.quantity]}')</script>")


class OrderAdmin(admin.ModelAdmin):
    actions = [export_to_excel, msg]


# Register the Order model with the custom admin class
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Validate)
admin.site.register(Prepare)
admin.site.register(ProductAvailability)
admin.site.register(Invoice)
admin.site.register(Aprovisinenemt)
admin.site.register(Test)
admin.site.register(InformeClient)
# Register your models here.
