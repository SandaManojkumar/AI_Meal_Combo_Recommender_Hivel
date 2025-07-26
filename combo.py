import pandas as pd
import numpy as np
import json
import streamlit as st

menu = pd.read_csv('AI_Menu_Items1.csv')

menu.rename(columns={
    'item_name': 'Item',
    'category': 'Category',
    'calories': 'Calories',
    'taste_profile': 'Taste',
    'popularity_score': 'Popularity'
}, inplace=True)

menu['Category'] = menu['Category'].str.lower()

def create_combos(day, data):
    mains = data[data['Category'] == 'main'].sample(4, random_state=50 + day).copy()
    sides = data[data['Category'] == 'side'].sample(3, random_state=100 + day).copy()
    drinks = data[data['Category'] == 'drink'].sample(3, random_state=200 + day).copy()

    mains.sort_values(by=['Calories', 'Popularity'], inplace=True)
    sides.sort_values(by=['Calories', 'Popularity'], inplace=True)
    drinks.sort_values(by=['Calories', 'Popularity'], inplace=True)

    combos = []
    for i in range(3):
        m = mains.iloc[i]
        s = sides.iloc[2 - i] 
        d = drinks.iloc[i]

        total_calories = int(m['Calories'] + s['Calories'] + d['Calories'])
        total_popularity = int((m['Popularity'] + s['Popularity'] + d['Popularity']) * 100)
        taste_combination = ', '.join([m['Taste'], s['Taste'], d['Taste']])

        combos.append({
            'combo_number': i + 1,
            'main_course': m['Item'],
            'side_course': s['Item'],
            'beverage': d['Item'],
            'total_calories': total_calories,
            'taste_profile': taste_combination,
            'total_popularity_score': total_popularity
        })

    return combos

days_output = {}
for day in range(1, 5):
    days_output[f'day_{day}'] = create_combos(day, menu)

api_output = json.dumps(days_output, indent=2)


st.title("AI Meal Combo Recommender")

st.markdown("""
This app generates **3 unique meal combos per day** for 4 days.
- Each combo has: 1 Main course, 1 Side course, 1 Beverage.
- Combos are balanced to have roughly equal **calories** and **popularity scores** per day.
- No repeats of items within a day.
- Taste profiles are also shown.
""")

day_selected = st.selectbox("Select Day", options=[f"day_{i}" for i in range(1, 5)])

st.subheader(f"Combos for {day_selected.capitalize()}")

combos_today = days_output[day_selected]

df_display = pd.DataFrame(combos_today)
df_display = df_display.rename(columns={
    'combo_number': 'Combo #',
    'main_course': 'Main Course',
    'side_course': 'Side Course',
    'beverage': 'Beverage',
    'total_calories': 'Calories',
    'taste_profile': 'Taste Profile',
    'total_popularity_score': 'Popularity Score'
})

st.table(df_display)

st.subheader("Raw JSON Output")
st.json(days_output[day_selected])

st.download_button(
    label="Download All Days Combos as JSON",
    data=api_output,
    file_name='meal_combos_output.json',
    mime='application/json'
)

