# Transformation Matrix Package

Our Transformation Matrix Package offers an intuitive and powerful solution for handling transformation matrices, with a special focus on 3D rotation matrices.
Primarily designed for engineers, designers, and those involved in three-dimensional object transformations, this Python package currently facilitates the
manipulation of Rotation Matrices to enable precise rotations within 3D space—a fundamental aspect of transformation matrices. As we continue to develop the tool,
we plan to expand its features to encompass a broader range of transformation matrix capabilities. A significant application of this tool lies in the engineering sector,
especially in accurately aligning Finite Element (FE) Models with global positions as illustrated in engineering drawings. This function proves to be particularly beneficial,
allowing engineers to adopt a more convenient coordinate system for model development before rotating it to the required orientation. This not only simplifies
the modeling process but also enhances the precision and reduces the complexity of design tasks.

## Introduction to Transformation Matrices

Transformation Matrices are powerful mathematical tools used in various fields such as computer graphics, physics, 
and engineering. They are matrices that represent different types of transformations in space, such as scaling, 
rotation, and translation. These matrices enable us to perform complex transformations in a straightforward and efficient manner.

### Rotation Matrices in 3D Space

Among the various types of transformation matrices, Rotation Matrices are particularly important. They are used to rotate 
objects in two-dimensional or three-dimensional space.
In three-dimensional space, a Rotation Matrix can rotate an object about the x, y, or z-axis. The formulation of a 3D 
rotation matrix depends on the axis and angle of rotation. The general form of these matrices is:

$$R_x(\theta) = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) \\
0 & \sin(\theta) & \cos(\theta)
\end{bmatrix}$$

$$R_y(\theta) = 
\begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) \\
0 & 1 & 0 \\
-\sin(\theta) & 0 & \cos(\theta)
\end{bmatrix}$$

$$R_z(\theta) = 
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}$$


Where (θ) is the angle of rotation.


---

- The program developed by: Pedram Manouchehri
- User interface developed by: Nam Nguyen 
- Independently checked by: [Name if applicable]
