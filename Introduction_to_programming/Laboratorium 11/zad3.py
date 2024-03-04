import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y_sin, color='blue', label='sin(x)')

plt.plot(x, y_cos, color='red', label='cos(x)')

# Ustawienie zakresu osi y
plt.ylim(-1, 1)

plt.xticks(np.arange(-2*np.pi, 2*np.pi+1, np.pi/2),
           ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π'])

plt.yticks([-1, 0, 1])

plt.title('Wykres funkcji sin(x) i cos(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
