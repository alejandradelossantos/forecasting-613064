
import plotly.graph_objects as go
import numpy as np

def graficar_serie(original, forecast, title):
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=original.index,
            y=original,
            mode='lines',
            name='Pasajeros_reales',
            opacity=0.5
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            mode='lines',
            name=title
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title='fecha',
        yaxis_title='num de pasajeros'
    )
    
    fig.show()

def mape(original, forecast):
    mask = forecast.notna()
    mape_value = np.mean(
        np.abs(
            (original[mask] - forecast[mask]) / original[mask]
        )
    )
    return mape_value