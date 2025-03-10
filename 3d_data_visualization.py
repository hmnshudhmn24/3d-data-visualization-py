import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_plot():
    """Generates an interactive 3D surface plot using Matplotlib."""
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Generate mesh grid
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Plot surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    # Labels
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Surface Plot')

    # Color bar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    plt.show()

if __name__ == "__main__":
    generate_3d_plot()
