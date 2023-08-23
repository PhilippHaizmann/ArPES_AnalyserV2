import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# Create the figure and axes
fig, ax = plt.subplots()

# Define the file and path for the image to be loaded
file = "fixed049_MoS2_CoPcF16_0364eV"
path = "C:/Users/Philipp/OneDrive - UT Cloud/Promotion/DatenUndAnalysen/MoS2_CoPc/BESSY/BESSY_Paper/Daten/MoS2_BandMaps/ImpulseMaps/"
img = plt.imread(path + file + ".png")

# Define the boundaries for the image display
x_min, x_max = -0.9948631, 1.2648937
y_min, y_max = -0.36491301, 1.894877

# Display the image and adjust axis labels
ax.imshow(img, cmap="viridis", aspect="auto", vmin=0.3, vmax=0.5, extent=[x_min, x_max, y_min, y_max])
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel("$k_{x} [A^{-1}]$")
ax.set_ylabel("$k_{y} [A^{-1}]$")

# Mark symmetry points on the graph
fontsize = 16
# Adding path_effects will provide a white stroke to make the text more visible against the background
path_effects = [pe.withStroke(linewidth=5, foreground='white')]
ax.text(0, 0, u"\u0393", fontsize=fontsize, path_effects=path_effects)
ax.text(-0.191, 1.322, "K", fontsize=fontsize, path_effects=path_effects)
ax.text(1.043, 0.863, "K'", fontsize=fontsize, path_effects=path_effects)
ax.text(0.451, 1.089, "M", fontsize=fontsize, path_effects=path_effects)

# Save the figure in both SVG and PNG formats
fig.savefig(path + file + "_final.svg", format="svg", dpi=500)
fig.savefig(path + file + "_final.png", format="png", dpi=500)

# Display the plot
plt.show()
