import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
from color import colors

telco_data = pd.read_csv('data/telco_customer.csv')
telco_data['TotalCharges'] = pd.to_numeric(
    telco_data['TotalCharges'], errors='coerce')
telco_data['Churn'] = telco_data['Churn'].apply(
    lambda x: 1 if x == 'Yes' else 0)
telco_data = telco_data.fillna(0)


fig1 = px.bar(telco_data, x="tenure", y="Churn",
              color="gender", barmode="group")
fig2 = px.scatter(telco_data, x="TotalCharges", y="MonthlyCharges",
                  size="tenure", color="PaymentMethod", hover_name="Churn",
                  log_x=True, size_max=60)
fig3 = {
    'data': [go.Heatmap(
        x=telco_data['Churn'],
        y=telco_data['TotalCharges'],
        z=telco_data['Churn'],
        colorscale='Viridis')],
    'layout': go.Layout(
        xaxis=dict(title='Churn'),
        yaxis=dict(title='TotalCharges'),
    )
}
fig4 = px.line(telco_data, x="MonthlyCharges", y="TotalCharges",
               title='TotalCharges V/S MonthlyCharges')
fig5 = px.line(telco_data, x="Churn", y="tenure", title='Churn V/S Tenure')
fig6 = px.line(telco_data, x="tenure", y="MonthlyCharges",
               title='Tenure V/S MonthlyCharges')

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig5.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
