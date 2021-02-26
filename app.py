import pandas as pd
import requests
import bar_chart_race as brc
import streamlit as st


def kerala_data():
    r = requests.get('https://keralastats.coronasafe.live/histories.json')

    json_data = r.json()
    all_data = json_data['histories']

    summary = [place['summary'] for place in all_data]

    kerala = []
    for item in summary:

        data = {}
        data['Alappuzha'] = item['Alappuzha']['confirmed']
        data['Ernakulam'] = item['Ernakulam']['confirmed']
        data['Idukki'] = item['Idukki']['confirmed']
        data['Kannur'] = item['Kannur']['confirmed']
        data['Kollam'] = item['Kollam']['confirmed']
        data['Kottayam'] = item['Kottayam']['confirmed']
        data['Kozhikode'] = item['Kozhikode']['confirmed']
        data['Malappuram'] = item['Malappuram']['confirmed']
        data['Palakkad'] = item['Palakkad']['confirmed']
        data['Pathanamthitta'] = item['Pathanamthitta']['confirmed']
        data['Thiruvananthapuram'] = item['Thiruvananthapuram']['confirmed']
        data['Thrissur'] = item['Thrissur']['confirmed']
        data['Wayanad'] = item['Wayanad']['confirmed']
        kerala.append(data)

    df = pd.DataFrame(kerala)
    df['dates'] = [day['date'] for day in all_data]
    df = df.set_index('dates')
    return df


kl_df = kerala_data()
charts = brc.bar_chart_race(df=kl_df, filename=None)

st.markdown('''
# Kerala Active Cases from January 2020 till Now using Steamlit and Python
Shown are the latest news.

**Credits**
- App built by [Baburaj R](https://wa.me/919567284082)
- Built in `Python` using `streamlit`.
''')
st.write('---')
st.write(charts)