import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 a& Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# write response code 200
# streamlit.text(fruityvice_response)

# Just print json
streamlit.text(fruityvice_response.json())

# take json version of response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Write on the screen
streamlit.dataframe(fruityvice_normalized)



