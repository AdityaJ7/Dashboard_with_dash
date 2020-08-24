import plotly
import lifelines
from datatable import data, T, E
from color import colors

kmffig = plotly.subplots.make_subplots(rows=2, cols=1, print_grid=False)
kmf = lifelines.KaplanMeierFitter()
kmf.fit(T, event_observed=E)
kmffig.append_trace(plotly.graph_objs.Scatter(x=kmf.survival_function_.index,
                                              y=kmf.survival_function_.values.flatten(), name="Kaplan Meier Survival"

                                              ),
                    1, 1)
kmffig.append_trace(plotly.graph_objs.Scatter(x=kmf.cumulative_density_.index,
                                              y=kmf.cumulative_density_.values.flatten(), name="Kaplan Meier Cumulative Density"
                                              ),
                    2, 1)
kmffig.update_layout(
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
