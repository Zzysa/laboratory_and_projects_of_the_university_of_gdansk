import matplotlib.pyplot as plt

with open('wynikiKolokwium.txt', 'r') as f:
    lines = f.readlines()

labels = []
sizes = []
for line in lines:
    ocena, liczba_osob = line.strip().split()
    labels.append(ocena)
    sizes.append(int(liczba_osob))

total = sum(sizes)
sizes = [100 * s / total for s in sizes]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Rozkład ocen na kolokwium')
plt.show()
