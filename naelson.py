import plotly
import lifelines
from datatable import data, T, E
from color import colors

naefig = plotly.subplots.make_subplots(rows=1, cols=1, print_grid=False)

nae = lifelines.NelsonAalenFitter()
nae.fit(T, event_observed=E)
naefig.append_trace(plotly.graph_objs.Scatter(x=nae.cumulative_hazard_.index,
                                              y=nae.cumulative_hazard_.values.flatten(), name="Nelson Aalen"

                                              ),
                    1, 1)


naefig.update_layout(
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
