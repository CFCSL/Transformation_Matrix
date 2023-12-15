# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:05:59 2023

@author: Pedram Manouchehri
"""

import numpy as np
import pandas as pd
import os


def rotation_matrix(theta):
    r_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta[0]), -np.sin(theta[0])],
        [0, np.sin(theta[0]), np.cos(theta[0])]
    ])
    r_y = np.array([
        [np.cos(theta[1]), 0, np.sin(theta[1])],
        [0, 1, 0],
        [-np.sin(theta[1]), 0, np.cos(theta[1])]
    ])
    r_z = np.array([
        [np.cos(theta[2]), -np.sin(theta[2]), 0],
        [np.sin(theta[2]), np.cos(theta[2]), 0],
        [0, 0, 1]
    ])
    r = np.dot(r_z, np.dot(r_y, r_x))
    return r


def apply_rotation(ndarray, r_matrix):
    new_array = np.dot(ndarray, r_matrix)
    return new_array


def apply_rotation_excel(io, angles, column_names=['X', 'Y', 'Z'], radians=False):
    if not radians:
        angles = np.radians(angles)
    r_matrix = rotation_matrix(angles)
    df = pd.read_excel(io, engine='openpyxl')
    if set(column_names).issubset(df.columns):
        ndarray = df[column_names].to_numpy()
        new_array = apply_rotation(ndarray, r_matrix)
        updated_column_names = [str(item) + '1' for item in column_names]
        df2 = pd.DataFrame(new_array, columns=updated_column_names)
        df3 = pd.concat([df, df2], axis=1)
        #df3.to_excel('output.xlsx', engine='openpyxl')
        return df3
    else:
        raise ValueError("column_names did not match!!")