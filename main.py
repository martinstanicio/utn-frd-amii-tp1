import os

import matplotlib.pyplot as plt
import numpy as np

ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = np.sqrt((X**2 + 1) * (Y**2 + 1))

# superficie
axes = plt.axes(projection="3d")
axes.plot_surface(X, Y, Z, cmap="viridis")

# intercambio los ejes x e y para que coincidan con lo visto en clase
axes.set_xlabel("y")
axes.set_ylabel("x")
axes.set_zlabel("z")

plt.savefig(
    os.path.join(ASSETS_DIR, "surface.png"),
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.3,
)
plt.close()

# curvas de nivel
contours = plt.contour(X, Y, Z, levels=15, cmap="viridis")
plt.clabel(contours)
plt.colorbar(contours, label="z = f(x, y)")

plt.xlabel("x")
plt.ylabel("y")

plt.savefig(
    os.path.join(ASSETS_DIR, "contour.png"),
    dpi=300,
    bbox_inches="tight",
)
plt.close()
