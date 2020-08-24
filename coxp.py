import plotly
import lifelines
import pandas as pd
from datatable import data
from color import colors


df_r = data.loc[:, ['tenure', 'Churn', 'gender', 'Partner', 'Dependents',
                    'PhoneService', 'MonthlyCharges', 'SeniorCitizen', 'StreamingTV']]

df_dummy = pd.get_dummies(df_r, drop_first=True)

cphfig = plotly.subplots.make_subplots(rows=1, cols=1, print_grid=False)
cph = lifelines.CoxPHFitter()
cph.fit(df_dummy, 'tenure', event_col='Churn')

cphfig.append_trace(plotly.graph_objs.Box(x=cph.confidence_intervals_.values,
                                          y=cph.confidence_intervals_.values.flatten(), name="Nelson Aalen"

                                          ),
                    1, 1)

cphfig.update_layout(
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
