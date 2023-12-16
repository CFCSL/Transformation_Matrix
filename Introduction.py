import streamlit as st
import numpy as np
from logo_header import *
from helper_functions import *

# Streamlit page configuration
st.set_page_config(page_title="Transformation Matrices", page_icon=":book:")

logo()
header()



# Title of the page
st.title("Understanding Transformation Matrices")

# Introduction to Transformation Matrices
st.header("What is a Transformation Matrix?")
st.write("""
A Transformation Matrix is a special kind of matrix that describes how to apply a specific transformation to a space or set of points. 
It is widely used in various fields like computer graphics, robotics, and physics. Common transformations include scaling, 
translation, and rotation.
""")

# Section on Rotation Matrices
st.header("Rotation Matrices")
st.write("""
A Rotation Matrix is a type of Transformation Matrix used to rotate a vector in a coordinate space. 
The rotation can be in two-dimensional or three-dimensional space. The matrix is constructed from the rotation angle 
and the axis of rotation (for 3D rotations).

In 2D space, a rotation matrix that rotates a point through an angle \\( \\theta \\) can be represented as:

\\[
\\begin{bmatrix}
\\cos(\\theta) & -\\sin(\\theta) \\\\
\\sin(\\theta) & \\cos(\\theta)
\\end{bmatrix}
\\]

In 3D space, we often use separate rotation matrices for rotations about the x, y, and z axes.
""")

# Interactive Rotation Matrix Calculator
st.header("Interactive Rotation Matrix Calculator")

# User input for the angle
angle = st.slider("Select the rotation angle (in degrees):", -180, 180, 0)

# Function to calculate the 2D rotation matrix
def calculate_rotation_matrix(angle_degrees):
    theta = np.radians(angle_degrees)  # Converting degrees to radians
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return rotation_matrix

# Calculating the rotation matrix for the given angle
rotation_matrix_2d = calculate_rotation_matrix(angle)

# Display the rotation matrix
st.write("The 2D rotation matrix for your selected angle is:")
st.latex(f"""
\\begin{{bmatrix}}
{rotation_matrix_2d[0,0]:.2f} & {rotation_matrix_2d[0,1]:.2f} \\\\
{rotation_matrix_2d[1,0]:.2f} & {rotation_matrix_2d[1,1]:.2f}
\\end{{bmatrix}}
""")


# Further Reading and References
st.subheader("Learn More")


st.markdown("""Ref""")

#---------------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown("""---
:bold[You can access the following to run your calculation in a more relaxed format by directly running the package locally]""")

# Path to your local Jupyter Notebook file
notebook_file_path = 'Notebook_transformation_matrix.ipynb'

# Read the notebook file as binary
with open(notebook_file_path, "rb") as file:
    btn = st.download_button(
            label="Download Jupyter Notebook",
            data=file,
            file_name=notebook_file_path ,
            mime="application/x-ipynb+json")


file_path = 'transformation_matrix.py'
# Read the package file as binary
with open(file_path, "rb") as file:
    btn = st.download_button(
            label="Download the Package",
            data=file,
            file_name=file_path ,
            mime="application/x-py+json")

#st.markdown("[Aerodynamic effect Python package](https://github.com/CFCSL/Transformation_Matrix)")
#---------------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
---
- The program developed by: 	Pedram Manouchehri
- User interface developed by:	Nam Nguyen 
- Independently checked by:		-
---
""")

