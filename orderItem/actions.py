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
    df = pd.read_excel('selected_orders.xlsx')
    print(df)
    # Generate an HTTP response to serve the Excel file for download
    with open('selected_orders.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="selected_orders.xlsx"'

    return response


export_to_excel.short_description = "Export  orders to Excel"


def export_invoice_to_excel(modeladmin, request, queryset):
    # Create a DataFrame from the selected orders
    data = {
        'Customer Name': [invoice.order.order.order.customer_name for invoice in queryset],
        'Product Name': [invoice.order.order.order.products.name for invoice in queryset],
        'Quantity': [invoice.order.order.order.quantity for invoice in queryset],
        'Price': [invoice.price for invoice in queryset],
        'Payment status': [invoice.C for invoice in queryset],
    }
    df = pd.DataFrame(data)

    # Create an Excel writer using pandas
    writer = pd.ExcelWriter('selected_Invoice.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Invoices', index=False)

    # Close the Pandas Excel writer
    writer.save()
    df = pd.read_excel('selected_Invoice.xlsx')
    print(df)
    # Generate an HTTP response to serve the Excel file for download
    with open('selected_Invoice.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="selected_Invoice.xlsx"'

    return response


export_invoice_to_excel.short_description = "Export  Invoice to Excel"
