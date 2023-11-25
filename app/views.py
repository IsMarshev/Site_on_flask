from app import application as pages
from flask import render_template, request, redirect, url_for, flash, make_response, session
import plotly.express as px
from programm.graphs import create_graph, create_pie
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pickle
import plotly.offline as pyo
import pandas as pd





@pages.route('/')
def home():
    return render_template('home.html')

@pages.route('/F1')
def F1():
    with open('app\imp1.pkl', 'rb') as file:
        feature_importances = pickle.load(file)
    with open("app\\names1.pkl", 'rb') as file:
        # Загружаем объект из файла
        feature_names = pickle.load(file)

    indices = feature_importances.argsort()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=feature_names[indices],
        x=feature_importances[indices],
        orientation='h',
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(color='rgba(50, 171, 96, 1.0)', width=1)
        )
    ))

    fig.update_layout(
        title='Важность признаков',
        yaxis=dict(title='Признак'),
        showlegend=False,
        height=300,
        margin=dict(l=20, r=20, t=30, b=30)
    )
    plot_html = pyo.plot(fig, output_type='div', config={'displayModeBar': False})


    


    with open("app\\fpr.pkl", 'rb') as file:
        fpr = pickle.load(file)
    with open('app\\tpr.pkl', 'rb') as file:
        tpr = pickle.load(file)
    with open('app\\thresholds.pkl', 'rb') as file:
        thresholds = pickle.load(file)
    with open('app\\roc_auc.pkl', 'rb') as file:
        roc_auc = pickle.load(file)

    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(x=fpr, y=tpr,
                            mode='lines',
                            name='ROC curve'.format(roc_auc),
                            line=dict(color='darkorange', width=2)))

    fig1.add_trace(go.Scatter(x=[0, 1], y=[0, 1],
                            mode='lines',
                            line=dict(color='navy', width=2, dash='dash'),
                            showlegend=False))

    fig1.update_layout(
        xaxis=dict(title='False Positive Rate'),
        yaxis=dict(title='True Positive Rate'),
        title='Receiver Operating Characteristic (ROC) Curve',
        legend=dict(x=0.01, y=0.99),
        height=300,
        margin=dict(l=20, r=20, t=30, b=30)
    )
    plot_html1 = pyo.plot(fig1, output_type='div', config={'displayModeBar': False})

    return render_template('F1.html', plot = plot_html, plot2 = plot_html1)

@pages.route('/RMSE')
def RMSE():
    with open('app\imp2.pkl', 'rb') as file:
        feature_importances = pickle.load(file)
    with open("app\\names2.pkl", 'rb') as file:
        feature_names = pickle.load(file)
        
    indices = feature_importances.argsort()
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=feature_names[indices],
        x=feature_importances[indices],
        orientation='h',
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(color='rgba(50, 171, 96, 1.0)', width=1)
        )
    ))

    fig.update_layout(
        title='Важность признаков',
        xaxis=dict(title='Важность признака'),
        yaxis=dict(title='Признак'),
        showlegend=False,
        height=600,
    )

    plot_html1 = pyo.plot(fig, output_type='div', config={'displayModeBar': False})

    return render_template('RMSE.html', plot = plot_html1)

@pages.route('/ROC')
def ROC():
    data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]}
    data2 = {
    'x': [4, 2, 3, 4, 5],
    'y': [10, 15, 11, 13, 14]}
    return render_template('ROC.html', plot = create_graph(data), plot2 = create_pie())

@pages.route('/analys')
def analys():
    with open("app\my_object_time_1.pickle", 'rb') as file:
        aggregated_data_cheque_data_1 = pickle.load(file)
    with open('app\my_object_time_0.pickle', 'rb') as file:
        aggregated_data_cheque_data_0 = pickle.load(file)
    
    with open("app\my_object_1.pickle", 'rb') as file:
        data_day = pickle.load(file)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=aggregated_data_cheque_data_1['date'], y=aggregated_data_cheque_data_1['revenue'], mode='lines+markers', name='Средний чек для 1'))

    fig.add_trace(go.Scatter(x=aggregated_data_cheque_data_0['date'], y=aggregated_data_cheque_data_0['revenue'], mode='lines', name='Средний чек для 0', line=dict(color='red')))

    fig.update_layout(title='График среднего чека',
                    xaxis_title='Дата',
                    yaxis_title='Средний чек')
    
    fig1 = px.bar(data_day, x='Day', y=['Value_1','Value_0'], color='Day',
             labels={'Value': 'Значение', 'Day': 'День недели'},
             title='Столбчатая диаграмма дней для типа пользователя')
    
    
    plot_html = pyo.plot(fig, output_type='div', config={'displayModeBar': False})
    plot_html2 = pyo.plot(fig1, output_type='div', config={'displayModeBar': False})


    return render_template('analys.html', plot=plot_html, plot1=plot_html2)

@pages.route('/Pred')
def Pred():
    return render_template('Pred.html')

@pages.route('/About')
def About():
    return render_template('About.html')

@pages.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*7)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res


@pages.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res
