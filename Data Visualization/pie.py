import pandas as pd
import matplotlib.pyplot as plt
import os

# Data
data = {
    'Produk': ['A', 'B', 'C', 'D'],
    'Jumlah_Terjual': [150, 80, 60, 110]
}
df = pd.DataFrame(data)

os.makedirs('materi', exist_ok=True)

# Bar chart
plt.figure(figsize=(8,6))
bars = plt.bar(df['Produk'], df['Jumlah_Terjual'], color='orange')


# Tambahkan nilai di atas batang
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, yval, ha='center', va='bottom')

plt.title('Grafik Penjualan Produk Bulan Mei')
plt.xlabel('Produk')
plt.ylabel('Jumlah Terjual')
plt.ylim(0, max(df['Jumlah_Terjual']) + 20)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('materi/bar_chart.png')
plt.show()
