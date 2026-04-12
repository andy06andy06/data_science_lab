import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x, y = np.mgrid[0:5:50j, 0:5:50j]
mu_x = 2.5
mu_y = 2.5
sigma_x = 1
sigma_y = 1
p = 0
z = 1/(2*np.pi*sigma_x*sigma_y*np.sqrt(1-p**2))*np.exp(-1/(2*(1-p**2))*((x-mu_x)**2/sigma_x**2+(y-mu_y)**2/sigma_y**2-2*p*(x-mu_x)*(y-mu_y)/(sigma_x)*(sigma_y)))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 0.7, 1]))
ax.tick_params(axis='both', which='major', labelsize=8)
ax.set_xlabel('X Label',fontsize=8)
ax.set_ylabel('Y Label',fontsize=8)
ax.set_zlabel('Z Label',fontsize=8)

plt.show()