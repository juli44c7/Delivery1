# import
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd



# Import from Excel file, 4 different sheets
df_customers = pd.read_excel("my_shop_data.xlsx", engine='openpyxl', sheet_name="customers")
df_order = pd.read_excel("my_shop_data.xlsx", engine='openpyxl', sheet_name="order")
df_employee = pd.read_excel("my_shop_data.xlsx", engine='openpyxl', sheet_name="employee")
df_products = pd.read_excel("my_shop_data.xlsx", engine='openpyxl', sheet_name="products")


def get_data():
    # Employee name
    df_employee['emp_name'] = df_employee['firstname'] + ' ' + df_employee['lastname']

    # Customers name
    df_products['prod_name'] = df_products['productname'] 


 # Data - Add: total, order, year, month
    df_order['total'] = df_order['unitprice'] * df_order['quantity']


    # ***************************************
    # Data - Relationer
    # ***************************************
    order = pd.merge(df_order, df_products, on='product_id')
    order = pd.merge(order, df_employee, on='employee_id')
    

    # Order - Select colomns
    order = order[['order_id', 
                'product_id', 'prod_name', 'type',
                'employee_id', 'emp_name', 
                'total']]

    # Retuner til app.py
    return order



