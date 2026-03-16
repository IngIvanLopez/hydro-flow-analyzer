import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def hydro_metrics(df):

    flow = df["flow"]

    results = {
        "mean_flow": flow.mean(),
        "max_flow": flow.max(),
        "min_flow": flow.min()
    }

    return results


def plot_flow_duration_curve(df):

    flow = df["flow"].sort_values(ascending=False).reset_index(drop=True)

    n = len(flow)
    exceedance = np.arange(1, n + 1) / (n + 1) * 100

    fig, ax = plt.subplots()

    ax.plot(exceedance, flow)
    ax.set_xlabel("Probabilidad de excedencia (%)")
    ax.set_ylabel("Caudal")
    ax.set_title("Curva de Duración de Caudales")

    ax.grid()

    return fig
