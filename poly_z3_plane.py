import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja funkcji
def funkcja(z):
    return (z - 1) * (z - 1j) * (z + 1j)

# Utworzenie siatki punktów w płaszczyźnie zespolonej
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Obliczenie wartości funkcji na siatce punktów
W = funkcja(Z)

# Wykres 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, np.abs(W), cmap='viridis')

# Ustawienia wykresu
ax.set_title('Wykres funkcji $(z-1)(z-i)(z+i)=0$ w przestrzeni zespolonej')
ax.set_xlabel('Część rzeczywista')
ax.set_ylabel('Część urojona')
ax.set_zlabel('Wartość funkcji')
ax.view_init(45, 240)  # Ustawienie kąta widzenia

plt.show()