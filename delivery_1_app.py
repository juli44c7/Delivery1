# ***************************************
# Imports
# ***************************************
# Dash
import dash
from dash import html
from dash import dcc


# Div.
import pandas as pd



# Plotly
import plotly.express as px


# ***************************************
# Get data
# ***************************************
import delivery_1
order = delivery_1.get_data()


# ***************************************
# Diagram - Employee Sales
# ***************************************
fig_employee = px.bar(order, 
    x='emp_name', y='total', 
    color='type', text='total', title='Sales by Employee',
    hover_data=[],
    labels={'total':'Total sales', 'emp_name':'Employee', 'type':'Product Type'})
fig_employee.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_employee.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

fig_products = px.bar(order,
    x='prod_name', y='total',  
    color='type', text='total', title='Sales by Products',
    hover_data=[],
    labels={'total':'Total sales', 'prod_name':'products', 'type':'Product Type'})
fig_products.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_products.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=45)

# ***************************************
# Activate the app
# ***************************************
#app = dash.Dash(__name__)

dash_app = dash.Dash(__name__)
app = dash_app.server

# ***************************************
# Layout
# ***************************************
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                children=[
                    html.Div(className='four columns div-user-controls',
                            children=[
                                html.H2('Sales dashboard')]),
                                

                  
                    html.Div(className='eight columns div-for-charts bg-grey',
                            children=[
                                dcc.Graph(id="sales_employee", figure=fig_employee),
                                dcc.Graph(id="sales_products", figure=fig_products)
                            ]
                    ),
                ]
            )
        ]
)



# ***************************************
# Run the app
# ***************************************
if __name__ == '__main__':
    dash_app.run_server(debug=True)