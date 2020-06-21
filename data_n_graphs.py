# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:11:45 2020

@author: Syamanthaka B
"""
import pandas as pd
import plotly.graph_objects as go

folio_config_all = pd.read_csv('data/folio_config.csv')
folio_config = folio_config_all[folio_config_all['status'] == 'Active']
tot_invest = folio_config['Cost per month'].sum()

whose_lst = list(folio_config.whose.unique())
whose_lst.append("All")


whose_vals = folio_config.groupby(['whose'])['Cost per month'].sum()



def individuals_inv(indivd):
    if indivd == 'All':
        indiv_folio = folio_config
        invst_amt = tot_invest
        n_funds = len(list(folio_config.Fund_name.unique()))
    else:
        indiv_folio = folio_config[folio_config['whose']==indivd]
        invst_amt = indiv_folio['Cost per month'].sum()
        n_funds = len(list(indiv_folio.Fund_name.unique()))
        
    indiv_tab = go.Figure(
        data=[go.Table(
        columnwidth = [100,70,50],
        header=dict(values=list([indiv_folio.columns[i] for i in [1,2,8]]),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[indiv_folio.iloc[:,i] for i in [1,2,8]],
                   fill_color='lavender',
                   align='left'))
        ]
    )
    indiv_tab.update_layout(
        title='Investments of ' + indivd,
        width=350, height=250,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    
   
    return indiv_tab, invst_amt, n_funds
indiv_table, ind_invest, n_funds = individuals_inv('All')

def indiv_pie():
    indiv_pie = go.Figure(
        data=[go.Pie(labels=whose_lst, values=whose_vals.values)]
    )
    indiv_pie.update_layout(
        width=200, height=150,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return indiv_pie
indiv_pie = indiv_pie()