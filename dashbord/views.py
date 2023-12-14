# Create your views here.
import pandas as pd
from django.shortcuts import render


def dashboard(request):
    # Assuming 'selected_orders.xlsx' is in the same directory as your Django app
    file_path = 'selected_orders.xlsx'

    try:
        df = pd.read_excel(file_path)
        # Pass the DataFrame to the template as 'data'
        return render(request, 'dashbord/dash.html', {'data': df})
    except pd.errors.EmptyDataError:
        # Handle empty file or other read errors
        error_message = "Error reading the Excel file."
        return render(request, 'dashbord/dash.html', {'error_message': error_message})
