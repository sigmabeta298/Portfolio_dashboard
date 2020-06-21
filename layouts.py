# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:37:40 2020

@author: Syamanthaka
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import data_n_graphs as grf

title = html.Div([
    dbc.Row(dbc.Col(html.Div("Investment Dashboard", className="navbar")))
])

#######################################################################
#*********************************************************************
leftside_col = dbc.Col([
    html.Div(["Select Individual",
    dcc.Dropdown(
        id='whose',
        options=[
            {'label': i.capitalize(), 'value': i} for i in grf.whose_lst],
        value="All"
    ),
    ]),
    html.Br(),
    html.Div(["Select Goal",
    dcc.Dropdown(
        id='goal',
        options=[
            {'label': i.capitalize(), 'value': i} for i in grf.whose_lst],
        value="All"
    ),
    ]),
    html.Br(),
    html.Div(["Select Folio",
    dcc.Dropdown(
        id='folio',
        options=[
            {'label': i.capitalize(), 'value': i} for i in grf.whose_lst],
        value="All"
    ),
    ]),
    html.Br(),
    html.Div(["Select Status Type",
    dcc.Dropdown(
        id='status_type',
        options=[
            {'label': i.capitalize(), 'value': i} for i in grf.whose_lst],
        value="All"
    ),
    ]),
], width=3)
#*********************************************************************
rt_first_row =dbc.Row([
    dbc.Col([
        dbc.Card(
            dbc.CardBody([
                html.H4("Total investment", className="card-title"),
                html.P(
                    grf.tot_invest,
                    className="card-text",
                )
            ]),
            style={"width": "15rem"},
        ),
        dbc.Card(
            dbc.CardBody([
                html.H4("Indiv investment", className="card-title"),
                html.P(
                    grf.ind_invest,
                    id='ind_inv',
                    className="card-text",
                )
            ]),
            style={"width": "15rem"},
        ),
        dbc.Card(
            dbc.CardBody([
                html.H4("# unique funds", className="card-title"),
                html.P(
                    grf.n_funds,
                    id='n_funds',
                    className="card-text",
                )
            ]),
            style={"width": "15rem"},
        ),
    ], width=3),
   
    dbc.Card(
        dbc.CardBody([
            html.H4("Pie Chart", className="card-title"),
            dcc.Graph(
                id='ind_pie',
                figure=grf.indiv_pie
            )
        ]),
        style={"width": "16rem"},
    ),

    dbc.Card(
        dbc.CardBody([
            dcc.Graph(
                id='ind_tab',
                figure=grf.indiv_table
            )
        ]),
        style={"width": "25rem"},
    )

])


rightside_col = dbc.Col([
    rt_first_row,
    html.Hr(),
], width=9)

#*********************************************************************
#Layout1
layout1 = html.Div([
    dbc.Container([
    dbc.Row([
        leftside_col,
        rightside_col    
    ]),
    ],fluid=True)
 ])

#*********************************************************************
layout2 = html.Div([
])