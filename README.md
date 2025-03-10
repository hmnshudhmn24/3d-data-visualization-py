# 3D Data Visualization

## Overview
This project generates **interactive 3D plots** using Matplotlib. It creates a **3D surface plot** using NumPy-generated data and visualizes it with **color mapping**.

## Features
- Generates a **3D surface plot** using `matplotlib` and `mpl_toolkits.mplot3d`.
- Uses NumPy to create a mesh grid for smooth visualization.
- Applies a **color map** to enhance visualization.
- Displays an **interactive 3D plot** that can be rotated and zoomed.

## Requirements
Ensure you have Python installed along with the following dependencies:
```
numpy
matplotlib
```
Install the required dependencies using:
```
pip install numpy matplotlib
```

## Usage
1. Run the script:
```
python 3d_data_visualization.py
```
2. An **interactive 3D surface plot** will be displayed.

## Example Output
A **3D surface plot** where the Z-values are calculated using the function:
```
Z = sin(sqrt(X^2 + Y^2))
```
The plot will be interactive, allowing rotation and zooming.

## License
This project is open-source and free to use for educational and personal purposes.
