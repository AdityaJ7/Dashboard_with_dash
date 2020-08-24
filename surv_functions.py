from lifelines import *
import matplotlib.pyplot as plt
import plotly.tools as tls
from datatable import data, T, E

fig, axes = plt.subplots(3, 2, figsize=(
    9, 7.5))

T = data['tenure']
E = data['Churn']

wbf = WeibullFitter().fit(T, E, label='WeibullFitter')
ef = ExponentialFitter().fit(T, E, label='ExponentialFitter')
lnf = LogNormalFitter().fit(T, E, label='LogNormalFitter')
llf = LogLogisticFitter().fit(T, E, label='LogLogisticFitter')
naf = GeneralizedGammaFitter().fit(T, E, label='GeneralizedGammaFitter')
spl = SplineFitter([6, 20, 40, 75]).fit(T, E, label='SplineFitter')

wbf.plot_survival_function(ax=axes[0][0])
ef.plot_survival_function(ax=axes[0][1])
lnf.plot_survival_function(ax=axes[1][0])
llf.plot_survival_function(ax=axes[1][1])
naf.plot_survival_function(ax=axes[2][0])
spl.plot_survival_function(ax=axes[2][1])
survi = plt.gcf()
