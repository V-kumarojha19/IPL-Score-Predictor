import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['Kolkata Knight Riders',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Royal Challengers Bangalore',
         'Sunrisers Hyderabad',
         'Punjab Kings',
         'Delhi Capitals',
         'Mumbai Indians',
         'Gujarat Titans',
         'Lucknow Super Giants']

cities = ['Bengalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Kochi', 'Indore', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Sharjah', 'Dubai', 'Rajkot', 'Kanpur', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

st.title('IPL Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    possible_bowling_team = [team for team in teams if team!= batting_team]
    if possible_bowling_team:
        bowling_team = st.selectbox('Select the Bowling Team', sorted(possible_bowling_team))
    else:
        st.error('Batting and Bowling teams can not be same.')


city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    overs = st.number_input('Overs Completed(should be >5)', min_value=0, max_value=20)
with col5:
    wickets = st.number_input('Wickets Out', min_value=0, max_value=20)

last_five = st.number_input('Runs Score in last 5 Overs',min_value=0)

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame({'batting_team':[batting_team], 'bowling_team':[bowling_team],
         'city':[city], 'current_score':[current_score],
         'balls_left':[balls_left], 'wickets_left':[wickets],
         'crr':[crr], 'last_five':[last_five]})

    result = pipe.predict(input_df)
    st.header('Predicted Score: ' + str(int(result[0])))
