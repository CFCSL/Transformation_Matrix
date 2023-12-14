# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:05:59 2023

@author: Pedram Manouchehri
"""
import numpy as np
import pandas as pd
import os


def RotationMatrix(theta) :
	R_x = np.array([[1,					0,					0	],
					[0,	np.cos(theta[0]),	-np.sin(theta[0])	],
					[0,	np.sin(theta[0]),	np.cos(theta[0])	]])
	R_y = np.array([[np.cos(theta[1]),	0,	np.sin(theta[1])],[0,	1,	0	],[-np.sin(theta[1]),	0,	np.cos(theta[1])]])
	R_z = np.array([[np.cos(theta[2]),	-np.sin(theta[2]),0],[np.sin(theta[2]),	np.cos(theta[2]),0],[0,	0,	1]])
	R = np.dot(R_z, np.dot( R_y, R_x ))
	return R

# function to calculate the dot products 
# vector times vector


def j(nparray,RMatrix):
	newArray=np.dot(nparray,RMatrix)
	return newArray
# Write a function to read an external excel and return the final result?

def generate(input_file_excel,theta): # theta in degrees
	# convert theta from degrees to radial
	theta=np.radians(theta)
	RMatrix=RotationMatrix(theta)
	# convert the input excel file into data array
	df=pd.read_excel(input_file_excel)
	if {"X", "Y", "Z"}.issubset(df.columns):
		df1=df[["Z", "Y","Z"]].to_numpy() 
		newArray=j(df1,RMatrix)
		df2=pd.DataFrame(newArray,columns=['x','y','z'])

		df3=pd.concat([df, df2], axis=1)
		df3=df3.drop(columns=["X","Y","Z"], axis=1)
		
		df3.to_excel('output.xlsx')
		
		return df3
		
	else:
		raise ValueError("Choose the three columns of x, y, z.")
		return None
		


input_file_excelr"Inputs/Pylon-Deformations-Original.xlsx"

#df=pd.read_excel(input_file_excel)

#theta=[0,0,30]

#generate(input_file_excel,theta)
	
	



# =============================================================================
# 
# RMatrix=RotationMatrix([0,0,np.radians(30)])
# 
# 
# 
# df=pd.read_excel(r"C:\Users\cfcpc2\Documents\GitHub\GitHub_CFC\Rotation_Matrix\Pylon-Deformations-Original.xlsx")
# df1=df[['u-X','u-Y','u-Z']]
# df1=df1.to_numpy()
# j=np.dot(df1,RMatrix)
# 
# df2=pd.DataFrame(j,columns=['u-X-global','u-Y-global','u-Z-global'])
# df3=pd.concat([df, df2], axis=1)
# 
# df3.to_excel(r"C:\Users\cfcpc2\Documents\GitHub\GitHub_CFC\Rotation_Matrix\Pylon_Deformations-GLOBAL-XX.xlsx")
# 
# 
# =============================================================================
