# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:05:59 2023

@author: Pedram Manouchehri
"""
import numpy as np
import pandas as pd


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
	np.dot(,RMatrix)
	return newArray
# Write a function to read an external excel and return the final result?

def generate(input_excel, output_file_name):
	



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
