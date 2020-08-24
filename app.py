import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from layouts import page_contact_layout, page_eda_layout, page_6_layout, page_5_layout, page_4_layout, page_3_layout, page_2_layout, page_1_layout
from datatable import generate_table, data
from color import colors
from navigation import navbar

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

# Home Page Layout --------------------------------------------------------------------

index_page = html.Div([


    html.Img(src=app.get_asset_url('my-image.png'), style={'height': '50%',
                                                           'width': '75%'}),
    html.Br(),
    html.H3("""What  proportion of a population  will survive past a certain time? Of those that survive,
         at what rate will they die or fail?How do particular circumstances or characteristics increase or decrease 
         the probability of survival?Are there differences in survival between groups (e.g., between those given a new 
         treatment while those with older treatment methods)? These questions often come into our mind and Survival 
         Analysis has the answer to it."""),
    html.Br(),

    html.H4(children='Telco Customer Dataset'),
    html.Div([generate_table(data)], style={
             'padding-left': '1%', 'padding-right': '3%'})

], style={'textAlign': 'center'})

# Callbacks
@app.callback(dash.dependencies.Output('page-eda-content', 'children'),
              [dash.dependencies.Input('page-eda-dropdown', 'value')])
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
# Proper Page display
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    elif pathname == '/page-5':
        return page_5_layout
    elif pathname == '/page-6':
        return page_6_layout
    elif pathname == '/page-eda':
        return page_eda_layout
    elif pathname == '/page-contact':
        return page_contact_layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)
