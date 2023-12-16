import streamlit as st
import numpy as np
from logo_header import *
from helper_functions import *

# Streamlit page configuration
st.set_page_config(page_title="Transformation Matrices", page_icon="🔄")

logo()
header()

# Page Title
st.title("Transformation Matrix Package")

# Introduction to the Package
st.write("""
Our Transformation Matrix Package offers an intuitive and powerful solution for handling transformation matrices, with a special focus on 3D rotation matrices.
Primarily designed for engineers, designers, and those involved in three-dimensional object transformations, this Python package currently facilitates the
manipulation of Rotation Matrices to enable precise rotations within 3D space—a fundamental aspect of transformation matrices. As we continue to develop the tool,
we plan to expand its features to encompass a broader range of transformation matrix capabilities. A significant application of this tool lies in the engineering sector,
especially in accurately aligning Finite Element (FE) Models with global positions as illustrated in engineering drawings. This function proves to be particularly beneficial,
allowing engineers to adopt a more convenient coordinate system for model development before rotating it to the required orientation. This not only simplifies
the modeling process but also enhances the precision and reduces the complexity of design tasks.""")

# Introduction to Transformation Matrices
st.header("Introduction to Transformation Matrices")
st.write("""
Transformation Matrices are powerful mathematical tools used in various fields such as computer graphics, physics, 
and engineering. They are matrices that represent different types of transformations in space, such as scaling, 
rotation, and translation. These matrices enable us to perform complex transformations in a straightforward and efficient manner.
""")

# Rotation Matrices in 3D Space
st.subheader("Rotation Matrices in 3D Space")

st.write("""
Among the various types of transformation matrices, Rotation Matrices are particularly important. They are used to rotate 
objects in two-dimensional or three-dimensional space.
In three-dimensional space, a Rotation Matrix can rotate an object about the x, y, or z-axis. The formulation of a 3D 
rotation matrix depends on the axis and angle of rotation. The general form of these matrices is:
""")
st.latex(r"""
R_x(\theta) = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) \\
0 & \sin(\theta) & \cos(\theta)
\end{bmatrix}
""")
st.latex(r"""
R_y(\theta) = 
\begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) \\
0 & 1 & 0 \\
-\sin(\theta) & 0 & \cos(\theta)
\end{bmatrix}
""")
st.latex(r"""
R_z(\theta) = 
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}
""")
st.markdown(r"Where ($\theta$) is the angle of rotation.")



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

