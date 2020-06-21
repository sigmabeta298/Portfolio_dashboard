# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:39:14 2020

@author: Syamanthaka
"""

import dash_html_components as html

from app import app
import layouts as lyt
import callbacks

app.layout = html.Div([
    lyt.title,
    lyt.layout1
])



if __name__ == '__main__':
    app.run_server(debug=False)