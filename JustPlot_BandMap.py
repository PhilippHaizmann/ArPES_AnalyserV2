import numpy as np
import matplotlib.pyplot as plt
from labellines import labelLines
from matplotlib.widgets import Slider, RadioButtons, Button
import csv
import matplotlib.colors as mcolors
import scipy.constants as const

# Create the figure and axes
fig, ax = plt.subplots()

file = "FILENAME"
# Load the image
path = "FILEPATH"
img = plt.imread(path+ file+".png")
x_min, x_max = -1.8093908, 1.8120516
y_min, y_max = 7, -1

# Display the image and adjust the axis labels
ax.imshow(img, cmap="viridis", aspect="auto", vmin=0.4, vmax=0.8, extent=[x_min, x_max, y_min, y_max])
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel("$k_{\parallel} [A^{-1}]$")
ax.set_ylabel("$E_{F}-E [eV]$")

# Draw vertical lines representing K, Γ (Gamma), and M
ax.axvline(x=-1.362421800195313, color='#CB8C1F', label="K", linewidth=3)
ax.axvline(x=0, color='#CB8C1F', label=u"\u0393", linewidth=3)
ax.axvline(x=1.191203195507812, color='#CB8C1F', label="M", linewidth=3)

# Draw horizontal lines representing E_F and VBM
ax.axhline(y=0, color='r', label="$E_{F}$", linewidth=1, linestyle="--")
ax.axhline(y=0.65625, color='r', label="VBM", linewidth=1, linestyle="--")

# Label the lines
labelLines(ax.get_lines(), align=False, yoffsets=0, color="k", fontsize=16)

# Save the figure in both SVG and PNG formats
fig.savefig(path + file + "_final.svg", format="svg", dpi=500)
fig.savefig(path + file + "_final.png", format="png", dpi=500)

# Display the plot
plt.show()
