import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC - Lina was here')

st.write('Hello, * World! * :sunglasses:')
st.write('Hello, * World! * :heart:')
st.write('Thank you so very much, * for all you do! * :pray:')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#Do this function once, so it won't load again
@st.cache_data
#all copy and paste from the slides
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
#change the widget to a text
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')
#change from done to the following 
data_load_state.text("Done! (using st.cache_data)")

#st.subheader('Raw data')
#st.write(data)
#change the above 2 lines to the following 
#if we don't want to display the raw data immediatley
#will use checkbox

if st.checkbox('Show raw data'):
   st.subheader('Raw data')
   st.write(data)

#chart
if st.checkbox('Show bar chart'):
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


st.subheader('Map of all pickups')
st.map(data)

if st.checkbox('Show map'):
  #hour_to_filter = 17
  #Change the above to the following line
  hour_to_filter = st.slider('hour', 0, 23, 17)
  filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

  st.subheader(f'Map of all pickups at {hour_to_filter}:00')
  st.map(filtered_data)
