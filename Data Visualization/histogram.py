import matplotlib.pyplot as plt

ages = [22, 25, 30, 22, 24, 27, 25, 33, 36, 29, 40, 41, 35, 28, 26, 30, 31, 22]

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of People')
plt.grid(True)
plt.show()