import plotly.express as px
def create_graph(data):
    fig = px.line(data, x='x', y='y', title='Пример графика Plotly')
    fig.update_layout(
        xaxis_title='Ось X',
        yaxis_title='Ось Y',
        font=dict(family='Arial', size=12, color='blue'),
        margin=dict(l=50, r=50, t=50, b=50),
        paper_bgcolor='lightgray',
    )
    plot_html = fig.to_html(full_html=False)
    return plot_html