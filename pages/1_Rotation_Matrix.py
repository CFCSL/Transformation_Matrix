# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:42:30 2023

@author: cfcpc2
"""

import streamlit as st
import transformation_matrix as tm
from logo_header import *
from helper_functions import *
from PIL import Image

logo()
header()

st.header("**Rotation matrix**")
st.markdown('---')
# Load an image from file
image = Image.open(r"Drawings/ESQUEMA_PROYECCION.png")
# Display the image
st.image(image,  width=400, caption='Cartesian system')


# Create three columns
col1, col2, col3 = st.columns(3)
with col1:
    theta_1 = st.number_input('$\\theta_x[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)

with col2:
    theta_2 = st.number_input('$\\theta_y[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)

with col3:
    theta_3 = st.number_input('$\\theta_z[degrees]=$', min_value=0.0, max_value=360.0, value=0.0)



theta=[np.radians(theta_1),np.radians(theta_2),np.radians(theta_3)]
RMatrix=tm.rotation_matrix(theta)
st.write(f'Rotation matrix:',RMatrix)

#--------------------------------------------------------------------------------------------------------------------
st.markdown('---')
st.subheader('**Import data** (Optional)')

st.session_state['table']=pd.DataFrame([[10,0,0],[0,10,0],[0,0,10]],columns=['X','Y','Z'])


Excel_input = st.checkbox('Excel Input')

if Excel_input:
	with open("Input-Output/Transformation-Matrix-Sample.xlsx", "rb") as fp:
		btn = st.download_button(label="Download Excel Template",data=fp,file_name="Transformation-Matrix-Sample.xlsx",mime="application/xlsx")
	
	uploaded_file = st.file_uploader("Choose a file")

	if uploaded_file is not None:
		st.write('Data preview')
		st.session_state['table'] = pd.read_excel(uploaded_file)
#--------------------------------------------------------------------------------------------------------------------
st.markdown('---')
st.subheader('**Input/Edit data**')
st.markdown('set column names:')

col1, col2, col3 = st.columns(3)
with col1:
	x =st.text_input("First axis","X",key="X")
with col2:
	y =st.text_input("Second axis","Y",key="Y")
with col3:
	z =st.text_input("Third axis","Z",key="Z")

st.markdown('Input/Edit data:')
df=st.data_editor(st.session_state['table'],num_rows="dynamic",hide_index=True,key='df') #,key=f'editor_{k}'

#--------------------------------------------------------------------------------------------------------------------
st.markdown('---')
st.header('**Results**')

angles=[theta_1,theta_2,theta_3]

if df is not None and all(col in df.columns for col in [x, y, z]):
	results=tm.apply_rotation_dataframe(df, angles, column_names=[x, y, z], radians=False)
	st.write(results)
	st.markdown(download_link(results, 'Rotation_Applied'), unsafe_allow_html=True)
else:
	st.error('Some of the indicated columns not found in the table. please revise the Column names!', icon="🚨")

