import plotly.express as px
import plotly.offline as pyo
import pandas as pd
def create_graph(data):
    fig = px.line(data, x='x', y='y', title='Пример графика Plotly', color_discrete_sequence=['#3C91E6'])
    fig.update_layout(
        xaxis_title='Ось X',
        yaxis_title='Ось Y',
        font=dict(family='Poppins, sans-serif', size=12, color='#342E37'),
        margin=dict(l=20, r=20, t=30, b=30),
        paper_bgcolor='#F9F9F9',
        plot_bgcolor= '#eee'
    )
    plot_html = pyo.plot(fig, output_type='div', config={'displayModeBar': False})
    return plot_html

def create_pie():
    df = pd.DataFrame({
        'fruit': ['apple', 'orange', 'banana'],
        'amount': [10, 15, 20]
    })

    # Создаем круговую диаграмму
    fig = px.pie(df, values='amount', names='fruit', title='Пример графика Plotly')

    fig.update_layout(
        font_family='Poppins, sans-serif',
        font_size=12,
        font_color='#342E37',
        margin=dict(l=20, r=20, t=30, b=30),
        height=300,
        paper_bgcolor='#F9F9F9',
        plot_bgcolor='#eee'
    )
    plot_html = pyo.plot(fig, output_type='div', config={'displayModeBar': False})
    # Возвращаем HTML-код для отображения графика
    return plot_html