# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:42:30 2023

@author: cfcpc2
"""

import streamlit as st
from Local_Rotation import *
from logo_header import *
from helper_functions import *
from PIL import Image

logo()
header()
st.markdown('---')
st.header("**Rotation matrix**")

# Load an image from file
image = Image.open(r"Drawings/ESQUEMA_PROYECCION.png")
# Display the image
st.image(image,  width=200)

# Create three columns
col1, col2, col3 = st.columns(3)
with col1:
    theta_1 = st.number_input('$\\theta_x[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)

with col2:
    theta_2 = st.number_input('$\\theta_y[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)

with col3:
    theta_3 = st.number_input('$\\theta_z[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)



theta=[np.radians(theta_1),np.radians(theta_2),np.radians(theta_3)]
RMatrix=RotationMatrix(theta)
st.write(f'Rotation matrix:',RMatrix)

st.markdown('---')

st.header('**Data**')

# Initialize df as None
#df = None

bt_Sample=st.button('SAMPLE', key='SAMPLE')




if bt_Sample:
	df = pd.read_excel(r'Inputs/Pylon-Deformations-Original.xlsx', engine='openpyxl')

	columns = df.columns.tolist()
	
	
	# Define default values - you can adjust these as needed
	default_x = 'x' if 'x' in columns else 0
	default_y = 'y' if 'y' in columns else 0
	default_z = 'z' if 'z' in columns else 0
	X=st.selectbox('Chose the initial $x$-coordinate', options= columns, index=default_x)
	Y=st.selectbox('Chose the initial $y$-coordinate', options= columns, index=default_y)
	Z=st.selectbox('Chose the initial $z$-coordinate', options= columns, index=default_z)
	df1=df[[X,Y,Z]].to_numpy()

	j=np.dot(df1,RMatrix)
	
	df2=pd.DataFrame(j,columns=['x','y','z'])

	df3=pd.concat([df, df2], axis=1)
	df3=df3.drop(columns=[X,Y,Z], axis=1)
	st.write('Transformation Data:')
	st.write(df3)
	# Create a download button
	st.markdown(download_link(df3, 'Excel Sample'), unsafe_allow_html=True)
	




uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_dict=pd.read_excel(uploaded_file,sheet_name=None, engine='openpyxl')
	for k in _dict:
		df=_dict[k]
		edited_df=st.data_editor(df,num_rows="dynamic")
		if edited_df is not None:
			columns=edited_df.columns
			X=st.selectbox('Chose the initial $x$-coordinate', options= columns)
			Y=st.selectbox('Chose the initial $y$-coordinate', options= columns)
			Z=st.selectbox('Chose the initial $z$-coordinate', options= columns)
			df1=edited_df[[X,Y,Z]].to_numpy()

			j=np.dot(df1,RMatrix)
			
			df2=pd.DataFrame(j,columns=['x','y','z'])

			df3=pd.concat([edited_df, df2], axis=1)
			df3=df3.drop(columns=[X,Y,Z], axis=1)
			st.write('Transformation Data:')
			st.write(df3)
			# Create a download button
			st.markdown(download_link(df3, 'Transformation Data'), unsafe_allow_html=True)
		






