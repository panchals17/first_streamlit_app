import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# streamlit.title('My Parents New Healthy Diner')
# streamlit.header('Breakfast Menu')
# streamlit.text('Omega 3 a& Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket')
# streamlit.text('Hard-Boiled Free-Range Egg')
# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#-----------------------------------------------------------
#---------------------Snowflakes----------------------------
#-----------------------------------------------------------
streamlit.title("Snowflakes Badge 2: Data Application Builders Workshop")
streamlit.subheader("Tech stack - Snowflakes, Python, REST API, Streamlit, Rivery")
streamlit.subheader("                                            - Bhavin Panchal")
streamlit.header("Task - 1 - Read data from Snowflakes")
streamlit.text("Snowflakes connection was created in streamlit app")
#-----------------------------------------------------------
#snowflakes related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
#-----------------------------------------------------------

#Add button to load the fruit
if streamlit.button('Get Fruit Load list (Read from Snowflakes)'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

# streamlit.stop()
#-----------------------------------------------------------
# snowflakes related function - Allow user to add fruits
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
    return "Thank you for adding " + new_fruit
#-----------------------------------------------------------
    
add_my_fruit = streamlit.text_input('What Fruit would you like to add (Write to Snowflakes)')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(back_from_function)
  
streamlit.header('Task - 2 - Read data from S3 text file') 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.text('Fancy picker was created using python lib called - streamlit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Pineapple','Cherries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#Function def
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
          # write response code 200
          # streamlit.text(fruityvice_response)
          # Just print json
          # streamlit.text(fruityvice_response.json())
    # take json version of response and normalize it
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#New section to display Fruityvice api response
streamlit.header("Task - 3 - Read JSON data from Fruityvice API")
try:
  fruit_choice = streamlit.text_input('What fruit would you like more information about? e.g. apple, banana', 'kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit name.")
  else:
    #streamlit.write('User entered', fruit_choice)
    back_from_function = get_fruitvice_data(fruit_choice)
    # Write on the screen
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()



# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
