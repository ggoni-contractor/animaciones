import plotly.express as px
import pandas as pd
import numpy as np
import streamlit

#df = px.data.gapminder()

df = pd.read_excel('data.xlsx')

fig = px.bar(df, 
    text='dato',
    y = 'dato', 
    x = 'opcion',
    color='opcion',
    animation_frame= 'hora',
    range_y=[0,np.max(df.dato)])

fig.update_traces(textfont_size=40, 
            textangle=0, 
            textposition="outside", 
            cliponaxis=False)

streamlit.plotly_chart(fig)