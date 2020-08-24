import dash_dangerously_set_inner_html
import dash_html_components as html
from exploratory import fig1, fig2, fig3, fig4, fig5, fig6
import dash_core_components as dcc
from naelson import naefig
from kaplan import kmffig
from custom import custom1, custom2
from coxp import cphfig
from cum_hazard import surgi
from surv_functions import survi
import plotly.tools as tls

# Contact Page Layout -----------------------------------------------

page_contact_layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/css/pp.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Contact Us</title>
    <style>
    .container{
            color: black;

            }
    </style>
</head>
<body background='static/img/back.jfif'>

    <div class="admin">
          <div class="card">
            <img src="static/img/akshat.jpg" style="width:100%;height:350px">
            <div class="container">
              <h2>Akshat Anand</h2>
              Admin
              <br>
              akshatanandmallik@gmail.com
              <ul>
                <li>
                  <a href="https://www.linkedin.com/in/akshatanand1999/" target="_blank">
                    <i class="fa fa-linkedin-square" style="font-size:36px;color:black"></i>
                  </a>
                </li>
                <li>
                  <a href="https://github.com/cipheraxat" target="_blank">
                    <i class="fa fa-github" style="font-size:36px;color:black"></i>
                  </a>
                </li>
            </ul>
            </div>
          </div>
    </div>
    <br>
    <br>
    <br>
    <br>
    <div class="mentor">
        <div class="mentor-card">
            <img src="static/img/rohan.jpg" style='width:100%;height:350px'>
            <div class="container">
                <h2>Rohan Mathur</h2>
                Mentor
                <br>
                rohanmathur0@gmail.com
                <ul>
                    <li>
                      <a href="https://www.linkedin.com/in/rohanmathur17" target="_blank">
                        <i class="fa fa-linkedin-square" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://github.com/RohanMathur17" target="_blank">
                        <i class="fa fa-github" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="mentor-card">
            <img src="static/img/ankur1.jpg" style="width:100%;height:350px">
            <div class="container">
                <h2>Ankur Chourasia</h2>
                Mentor
                <br>
                chourasia.ankur1@gmail.com
                <ul>
                    <li>
                      <a href="https://www.linkedin.com/in/ankur-chourasia-790783145" target="_blank">
                        <i class="fa fa-linkedin-square" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://github.com/chourasiaankur1" target="_blank">
                        <i class="fa fa-github" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <br>
    <br>
    <br>
    <br>
    <div class="participant">
        <div class="participant-card">
            <img src="static/img/abhijit.jpg" style="width:100%;height:350px">
            <div class="container">
                <h2>Abhijit Tripathy</h2>
                Participant
                <br>
                abhijittripathy99@gmail.com
                <ul>
                    <li>
                      <a href="https://www.linkedin.com/in/abhijit-tripathy-415912187" target="_blank">
                        <i class="fa fa-linkedin-square" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://github.com/Abhijit2505" target="_blank">
                        <i class="fa fa-github" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="participant-card">
            <img src="static/img/aditya.jpg" style="width:100%">
            <div class="container">
                <h2>Aditya Jetely</h2>
                Participant
                <br>
                ajetely@gmail.com
                <ul>
                    <li>
                      <a href="https://www.linkedin.com/in/aditya-jetley" target="_blank">
                        <i class="fa fa-linkedin-square" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://github.com/AdityaJ7" target="_blank">
                        <i class="fa fa-github" style="font-size:36px;color:black"></i>
                      </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>

</body>
</html>

    '''),

    html.Div(id='my-div')
])


# EDA Page Layout -------------------------------------------------------------------------

page_eda_layout = html.Div([
    html.H1('Exploratory Data Analysis - Survival Data', style={'font-family': 'monospace', 'padding': '5%', 'background-color': 'black', 'color': '#7FDBFF', 'fontSize': 34},
            className=" twelve columns"),
    dcc.Graph(
        id='example-graph-2',
        figure=fig1
    ),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig2
    ),
    dcc.Graph(id='line-graph-1',
              figure=fig4),
    dcc.Graph(id='line-graph-2',
              figure=fig5),
    dcc.Graph(id='line-graph-3',
              figure=fig6),
    dcc.Graph(id='heatmap',
              figure=fig3),
    html.Div(id='page-eda-content'), ], style={'background-color': 'black'})

# Page 6 Layout -------------------------------

page_6_layout = html.Div([
    html.Div(className='row',
             children=[

                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Nelson Aalen Estimator'),
                         html.Hr(),
                         html.P(
                             '''This section contains the nelson aalen implementations which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "The Nelson-Aalen approach can quickly give you a curve of cumulative hazard and estimate the hazard functions based on irregular time intervals."),
                         html.H4(
                             "Nelson-Aalen analysis is used to analyze how a given population evolves with time."),
                         html.H4(
                             "Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.")
                     ]),
                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Nelson Aalen plots on the teleco dataset'), dcc.Graph(id='naeplot',
                                                                                                                                                config={
                                                                                                                                                    'displayModeBar': False},
                                                                                                                                                animate=True,
                                                                                                                                                figure=naefig
                                                                                                                                                ), ])
             ]),
    html.Div(id='page-6-content'),

])

# Page 5 Layout ----------------------------

page_5_layout = html.Div([
    html.Div(className='row',
             children=[

                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Kaplan Meier Curves'),
                         html.Hr(),
                         html.P(
                             '''This section contains the kaplan meier implementations which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "Kaplan-Meier estimate is one of the best options to be used to measure the fraction of subjects living for a certain amount of time after treatment."),
                         html.H4(
                             " In clinical trials or community trials, the effect of an intervention is assessed by measuring the number of subjects survived or saved after that intervention over a period of time."),
                         html.H4(
                             "Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.")
                     ]),

                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Kaplan Meier Survival Function and Cumalative density plots on the teleco dataset'), dcc.Graph(id='kmfplot',
                                                                                                                                                                                         config={
                                                                                                                                                                                             'displayModeBar': False},
                                                                                                                                                                                         animate=True,
                                                                                                                                                                                         figure=kmffig
                                                                                                                                                                                         ), ])
             ]),
    html.Div(id='page-5-content'),

])

# Page 4 Layout ----------------------------

page_4_layout = html.Div([
    html.Div(className='row',
             children=[

                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Custom Models'),
                         html.Hr(),
                         html.P(
                             '''This section contains the custom models which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "The custom models are used to obtain survival functions and cumulative hazards by using univariate filter in the adjacent visualization"),
                         html.H4(
                             "Two and three paramater custom models have been visualized here."),
                     ]),

                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Custom model implementation on the teleco dataset - 3 Parameters'), dcc.Graph(id='custom',
                                                                                                                                                                        config={
                                                                                                                                                                            'displayModeBar': False},
                                                                                                                                                                        animate=True,
                                                                                                                                                                        figure=custom1
                                                                                                                                                                        ), html.H2('Custom model implementation on the teleco dataset - 2 Parameters'), dcc.Graph(id='custom',
                                                                                                                                                                                                                                                                  config={
                                                                                                                                                                                                                                                                      'displayModeBar': False},
                                                                                                                                                                                                                                                                  animate=True,
                                                                                                                                                                                                                                                                  figure=custom2
                                                                                                                                                                                                                                                                  )])
             ]),
    html.Div(id='page-4-content'),

])

# Page 3 Layout --------------------------

page_3_layout = html.Div([
    html.Div(className='row',
             children=[

                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Cox Proportional Model'),
                         html.Hr(),
                         html.P(
                             '''This section contains the cox proportional model which is made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "In his seminal paper, Cox (1972) presented the proportional hazards model."),
                         html.H4(
                             "It specifies that the conditional hazard function of failure time given a set of covariates is the product of an unknown baseline hazard function and an exponential regression function of covariates"),
                     ]),

                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Cox Proportional Hazard Model on the teleco dataset'), dcc.Graph(id='coxproportional',
                                                                                                                                                           config={
                                                                                                                                                               'displayModeBar': False},
                                                                                                                                                           animate=True,
                                                                                                                                                           figure=cphfig
                                                                                                                                                           ), ])
             ]),
    html.Div(id='page-3-content'),

])

# Page 2 Layout ------------------------------------

page_2_layout = html.Div([
    html.Div(className='row',
             children=[
                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Cumulative Hazard Models'),
                         html.Hr(),
                         html.P(
                             '''This section contains the cumulative hazard models which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "The time to event of the teleco dataset has been modelled using the four different parametric models."),
                         html.H4(
                             "Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.")
                     ]),

                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Parametric Model Implementation of cumulative hazard function on the Telco dataset'), dcc.Graph(id='hazardfunction',
                                                                                                                                                                                          config={
                                                                                                                                                                                              'displayModeBar': False},
                                                                                                                                                                                          animate=True,
                                                                                                                                                                                          figure=tls.mpl_to_plotly(surgi, resize=True).update_layout(
                                                                                                                                                                                              {'plot_bgcolor': 'rgba(102,204,255,0)',
                                                                                                                                                                                               'paper_bgcolor': 'rgba(255, 255, 255, 0 )'})
                                                                                                                                                                                          ), dcc.Markdown("""
                                                                                                                                                                                          ##### The dataset used in this visualization is https://github.com/AdityaJ7/Parametric-models/blob/master/Dataset/telco_customer.csv"""),

                                                                                 dcc.Markdown(
                                                                                     """##### The time to event of the teleco dataset has been modelled using the four different parametric models."""),
                                                                                 dcc.Markdown("""##### Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.""")])
             ]),
    html.Div(id='page-2-content'),


])

# Page 1 Layout ------------------

page_1_layout = html.Div([
    html.Div(className='row',
             children=[
                 html.Div(
                     className='four columns div-user-controls', children=[
                         html.H1('Survival Functions '),
                         html.Hr(),
                         html.P(
                             '''This section contains the survival functions which are made using lifelines and plotly modules.'''),
                         html.Hr(),
                         html.H4(
                             "The survival function using the parametric models is shown in the adjacent visualization"),
                         html.H4(
                             "The time to event of the teleco dataset has been modelled using the four different parametric models."),
                         html.H4(
                             "Here the time is the tenure(in months) for which the customer stayed in the company and the event is whether they churned or not.")
                     ]),

                 html.Div(
                     className='eight columns div-for-charts bg-grey', children=[html.H2('Implementation of  Paramteric Models to create survival functions on the teleco dataset'), dcc.Graph(id='survivalfunction',
                                                                                                                                                                                               config={
                                                                                                                                                                                                   'displayModeBar': False},
                                                                                                                                                                                               animate=True,
                                                                                                                                                                                               figure=tls.mpl_to_plotly(survi, resize=True).update_layout(
                                                                                                                                                                                                   {'plot_bgcolor': 'rgba(102,204,255,0)',
                                                                                                                                                                                                    'paper_bgcolor': 'rgba(255, 255, 255, 0 )',
                                                                                                                                                                                                    })
                                                                                                                                                                                               ),


                                                                                 ])
             ]),
    html.Div(id='page-1-content'),

])
