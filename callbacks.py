# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:11:45 2020

@author: Syamanthaka
"""

from dash.dependencies import Input, Output

from app import app
import layouts as lyt
import data_n_graphs as grf

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return lyt.layout1
    elif pathname == '/apps/app2':
         return lyt.layout2
    else:
        return '404'
    
@app.callback([Output('ind_tab', 'figure'),
               Output('ind_inv', 'children'),
               Output('n_funds', 'children')],
              [Input('whose', 'value')])
def select_indv_details(whose):
    whose_table, ind_inv, n_funds = grf.individuals_inv(whose)
    return whose_table, ind_inv, n_funds