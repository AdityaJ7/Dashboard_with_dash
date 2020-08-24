T = data['tenure']
E = data['Churn']
fig = make_subplots(rows=1, cols=1, print_grid=False)
fig.append_trace(go.Scatter(), 1, 1)
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis=dict(
        title="Time Period"
    ),
    yaxis=dict(
        title="Churning Probability"
    )
)
available_parameters = ["WeibullFitter", "ExponentialFitter", "LogNormalFitter",
                        "LogLogisticFitter", "GeneralizedGammaFitter", "SplineFitter"]


opts = [{'label': i, 'value': i} for i in available_parameters]


page_1_layout = html.Div([
    html.Div(className='row',
             children=[

                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Survival Functions with Python'),
                         html.Hr(),
                         html.P(
                             '''This section contains the survival functions which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "The survival function using the parametric models is shown in the above visualization"),
                         html.H4(
                             "The time to event of the teleco dataset has been modelled using the four different parametric models."),
                         html.H4(
                             "Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.")
                     ]),
                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[

                         html.P([
                             html.Label(
                                 "Choose a parametric model"),
                             dcc.Dropdown(id='opt',
                                          options=[{'label': i, 'value': i}
                                                   for i in available_parameters],
                                          value='')
                         ], style={'width': '400px',
                                   'fontSize': '20px',
                                   'padding-left': '100px',
                                   'display': 'inline-block'}),


                         dcc.Graph(id='plot',
                                   config={
                                       'displayModeBar': False},
                                   animate=True,
                                   figure=fig
                                   ),
                     ])
             ]),

])


@app.callback(dash.dependencies.Output('plot', 'figure'),
              [dash.dependencies.Input('opt', 'value')])
def update_figure(input_value):
    if input_value == "WeibullFitter":

        kmf = WeibullFitter()
        kmf.fit(T, event_observed=E, label=input_value)

    elif input_value == "ExponentialFitter":

        kmf = ExponentialFitter()
        kmf.fit(T, event_observed=E, label=input_value)

    elif input_value == "LogNormalFitter":
        kmf = LogNormalFitter()
        kmf.fit(T, event_observed=E, label=input_value)
    elif input_value == "LogLogisticFitter":
        kmf = LogLogisticFitter()
        kmf.fit(T, event_observed=E, label=input_value)
    elif input_value == "GeneralizedGammaFitter":

        kmf = GeneralizedGammaFitter()
        kmf.fit(T, event_observed=E, label=input_value)
    elif input_value == "SplineFitter":

        kmf = SplineFitter([6, 20, 40, 75])
        kmf.fit(T, event_observed=E, label=input_value)

    fig.data = []
    fig.append_trace(go.Scatter(x=kmf.survival_function_.index,
                                y=kmf.survival_function_.values.flatten(), name=input_value

                                ),
                     1, 1)
    return fig
