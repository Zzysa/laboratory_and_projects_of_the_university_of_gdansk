import numpy as np
import matplotlib.pyplot as plt

n = int(input("Podaj liczbę rzutów monetą (n): "))
p = float(input("Podaj prawdopodobieństwo wyrzucenia (0 < p < 1): "))
s = int(input("Podaj liczbę prób (s): "))

results = np.random.binomial(n, p, s)

plt.hist(results, bins=range(n+2), align='left', rwidth=0.8, color='blue', edgecolor='black')

plt.title('Rozkład rzutu monetą')
plt.xlabel('Liczba orłów')
plt.ylabel('Liczba prób')
plt.show()
