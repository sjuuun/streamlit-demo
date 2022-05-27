"""
# My first app
Here's our first attempt at using data to create a table:
"""

import time

import numpy as np
import pandas as pd
import streamlit as st

#####
# Use magic
df = pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
})

'Display using magic:'
df

#####
# Write a data frame
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
}))

#####
# Magic vs Write
df = pd.DataFrame(
	np.random.randn(10, 20),
	columns=('col %d' % i for i in range(20))
)

st.write('Display dataframe with style:')
st.dataframe(df.style.highlight_max(axis=0))

#####
# Draw line chart
chart_data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a', 'b', 'c']
)

st.write('Display dataframe to line chart:')
st.line_chart(chart_data)

#####
# Plot a map
map_data = pd.DataFrame(
	np.random.randn(1000, 2) / [50, 50] + [37.5, 127.0],
	columns=['lat', 'lon']
)

st.write('Display dataframe to map:')
st.map(map_data)

#####
# Simple Widget
st.write('Slider Widget:')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write('Text Input Widget:')
st.text_input("Your name", key="name")
st.write(f'Hello, {st.session_state.name}')

#####
# Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
	chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c']
	)

	chart_data

#####
# Use a selectbox for options
df = pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
})

option = st.selectbox(
	'Which number do you like best?',
	df['first column']
)
st.write(f'You selected: {option}')

#####
# Sidebar Layout
add_selectbox = st.sidebar.selectbox(
	'How would you like to be contacted?',
	('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
	'Select a range of values',
	0.0, 100.0, (25.0, 75.0)
)

#####
# Column Layout
left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
	chosen = st.radio(
		'Sorting hat',
		("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
	st.write(f"You are in {chosen} house!")

#####
# Show Progress

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
	# Update the progress bar with each iteration.
	latest_iteration.text(f'Iteration {i + 1}')
	bar.progress((i + 1) * 10)
	time.sleep(0.1)

'...and now we\'re done!'
