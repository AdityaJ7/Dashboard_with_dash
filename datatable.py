import pandas as pd
import dash_html_components as html

data = pd.read_csv('data/telco_customer.csv')
data['tenure'] = pd.to_numeric(data['tenure'])
data = data[data['tenure'] > 0]

# Replace yes and No in the Churn column to 1 and 0. 1 for the event and 0 for the censured data.
data['Churn'] = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
T = data['tenure']
E = data['Churn']


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
