import matplotlib.pyplot as plt 
import numpy as np 
# Jesus Ariaga NC 0019
cant_productos=[200,280,300,350,400]
precio=[4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

# personalizar grafica
plt.plot(cant_productos, precio, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.title("Ventas de walmart 0019")
plt.xlabel("Cant productos")
plt.ylabel("Precios")
plt.show()