import dash_html_components as html
import dash_core_components as dcc
import plotly
import lifelines
import numpy as np
from datatable import data, T, E
from lifelines.fitters import ParametricUnivariateFitter
from color import colors


class ThreeParamInverseTimeHazardFitter(ParametricUnivariateFitter):

    _fitted_parameter_names = ['alpha_', 'beta_', 'gamma_']
    _bounds = [(0, None), (75.0001, None), (0, None)]

    # this is the only function we need to define. It always takes two arguments:
    #   params: an iterable that unpacks the parameters you'll need in the order of _fitted_parameter_names
    #   times: a numpy vector of times that will be passed in by the optimizer
    def _cumulative_hazard(self, params, times):
        a, b, c = params
        return a / (b - times) ** c


class TwoParamInverseTimeHazardFitter(ParametricUnivariateFitter):

    _fitted_parameter_names = ['alpha_', 'beta_']

    # Sequence of (min, max) pairs for each element in x. None is used to specify no bound
    _bounds = [(0, None), (75.0001, None)]

    def _cumulative_hazard(self, params, times):
        alpha, beta = params
        return alpha / (beta - times)


custom1 = plotly.subplots.make_subplots(rows=2, cols=1, print_grid=False)

new_timeline = np.arange(0, 80)

cus = ThreeParamInverseTimeHazardFitter().fit(T, E, timeline=new_timeline)

custom1.append_trace(plotly.graph_objs.Scatter(x=cus.cumulative_hazard_.index,
                                               y=cus.cumulative_hazard_.values.flatten(), name="Cumulative Hazard"

                                               ),
                     1, 1)
custom1.append_trace(plotly.graph_objs.Scatter(x=cus.survival_function_.index,
                                               y=cus.survival_function_.values.flatten(), name="Survival Function"

                                               ),
                     2, 1)


custom2 = plotly.subplots.make_subplots(rows=2, cols=1, print_grid=False)

new_timeline = np.arange(0, 80)

cus2 = TwoParamInverseTimeHazardFitter().fit(T, E, timeline=new_timeline)

custom2.append_trace(plotly.graph_objs.Scatter(x=cus2.cumulative_hazard_.index,
                                               y=cus2.cumulative_hazard_.values.flatten(), name="Cumulative Hazard"

                                               ),
                     1, 1)
custom2.append_trace(plotly.graph_objs.Scatter(x=cus2.survival_function_.index,
                                               y=cus2.survival_function_.values.flatten(), name="Survival Function"

                                               ),
                     2, 1)

custom1.update_layout(
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

custom2.update_layout(
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
