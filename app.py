# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:36:07 2020

@author: Syamanthaka
"""

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, 
                suppress_callback_exceptions=True, 
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server