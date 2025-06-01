import matplotlib.pyplot as plt
import pandas as pd

# Contoh data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Ad_Cost': [1000, 1500, 2000, 1800, 2200],      # Biaya iklan
    'Sales': [120, 160, 210, 190, 250],             # Unit terjual
    'Reach': [3000, 5000, 8000, 7000, 9000]          # Jumlah orang yang lihat iklan
}

df = pd.DataFrame(data)

plt.figure(figsize=(7,5))
scatter = plt.scatter(
    df['Ad_Cost'], 
    df['Sales'], 
    s=df['Reach'] / 10,             # Ukuran titik berdasarkan reach
    c=df['Reach'],                  # Warna juga berdasarkan reach
    cmap='rainbow', 
    alpha=0.7, 
    edgecolor='black'
)

# Tambahkan label ke setiap titik
for i, row in df.iterrows():
    plt.text(row['Ad_Cost'] + 30, row['Sales'] + 2, row['Product'], fontsize=9)

plt.colorbar(scatter, label='Ad Reach')
plt.title('Sales vs Advertising Cost with Reach Bubble')
plt.xlabel('Advertising Cost ($)')
plt.ylabel('Sales (units)')
plt.grid(True)
plt.tight_layout()
plt.show()
