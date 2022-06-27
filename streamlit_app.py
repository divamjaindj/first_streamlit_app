import streamlit

streamlit.title('My parents new healthier diner')

streamlit.header('Menu deko')

streamlit.text('🍞 Chole bhature')
streamlit.text('🥗 Masala Dosa')
streamlit.text('🥑 Omlette')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
