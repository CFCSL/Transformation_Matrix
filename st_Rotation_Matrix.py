# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:42:30 2023

@author: cfcpc2
"""

import streamlit as st
from Local_Rotation import *
from logo_header import *
from helper_functions import *

logo()
header()

st.header("**Rotation matrix**")

theta_1=st.number_input("$\\theta_1[degrees]=$", value=0.0, max_value= 90.0)
theta_2=st.number_input("$\\theta_2[degrees]=$", value=0.0, max_value= 90.0)
theta_3=st.number_input("$\\theta_3[degrees]=$", value=30.0, max_value= 90.0)
	
RMatrix=RotationMatrix([np.radians(theta_1),np.radians(theta_2),np.radians(theta_3)])
st.write(f'Rotation matrix:',RMatrix)

st.markdown('---')

st.header('**Data**')
st.markdown('---')
# Initialize df as None
#df = None

bt_Sample=st.button('SAMPLE', key='SAMPLE')




if bt_Sample:
	df=pd.read_excel(r'Pylon-Deformations-Original.xlsx')
	st.write(df)
	columns=df.columns
	X=st.selectbox('Chose the initial $x$-coordinate', options= "X")
	Y=st.selectbox('Chose the initial $y$-coordinate', options= "Y")
	Z=st.selectbox('Chose the initial $z$-coordinate', options= "Z")
	df1=df[[X,Y,Z]].to_numpy()

	j=np.dot(df1,RMatrix)
	
	df2=pd.DataFrame(j,columns=['x','y','z'])

	df3=pd.concat([df, df2], axis=1)
	df3=df3.drop(columns=[X,Y,Z], axis=1)
	st.write('Transformation Data:')
	st.write(df3)
	# Create a download button
	st.markdown(download_link(df3, 'Excel Sample'), unsafe_allow_html=True)
	

st.markdown('---')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_dict=pd.read_excel(uploaded_file,sheet_name=None)
	for k in _dict:
		df=_dict[k]
		st.write(df)
		if df is not None:
			columns=df.columns
			X=st.selectbox('Chose the initial $x$-coordinate', options= columns)
			Y=st.selectbox('Chose the initial $y$-coordinate', options= columns)
			Z=st.selectbox('Chose the initial $z$-coordinate', options= columns)
			df1=df[[X,Y,Z]].to_numpy()

			j=np.dot(df1,RMatrix)
			
			df2=pd.DataFrame(j,columns=['x','y','z'])

			df3=pd.concat([df, df2], axis=1)
			df3=df3.drop(columns=[X,Y,Z], axis=1)
			st.write('Transformation Data:')
			st.write(df3)
			# Create a download button
			st.markdown(download_link(df3, 'Transformation Data'), unsafe_allow_html=True)
		






