import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji
def funkcja(z):
    return (z - 1) * (z - 1j) * (z + 1j)

# Utworzenie siatki punktów w płaszczyźnie zespolonej
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Wykres funkcji
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, np.abs(funkcja(Z)), levels=[0, 0.1], colors='blue', alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)  # Dodanie osi rzeczywistej
plt.axvline(0, color='black', linewidth=0.5)  # Dodanie osi urojonej
plt.title('Wykres funkcji $(z-1)(z-i)(z+i)=0$ w płaszczyźnie zespolonej')
plt.xlabel('Część rzeczywista')
plt.ylabel('Część urojona')
plt.grid(True)
plt.show()