import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Units_Sold': [150, 80, 60, 110, 50]
}
df = pd.DataFrame(data)

# Prepare figure and 2 subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 5))  # 1 baris, 2 kolom

# --- Bar Chart ---
axs[0].bar(df['Product'], df['Units_Sold'], color='skyblue')
axs[0].set_title('Bar Chart')
axs[0].set_xlabel('Product')
axs[0].set_ylabel('Units Sold')

# --- Pie Chart ---
axs[1].pie(df['Units_Sold'], labels=df['Product'], autopct='%1.1f%%', startangle=90)
axs[1].set_title('Pie Chart')
axs[1].axis('equal')

# --- Line Chart ---
axs[2].plot(df['Product'], df['Units_Sold'], marker='o', linestyle='-', color='green')
axs[2].set_title('Line Chart')
axs[2].set_xlabel('Product')
axs[2].set_ylabel('Units_Sold')

# Save & Show
plt.tight_layout()
plt.savefig('output/subplots_chart.png')
plt.show()

# | Kode                 | Arti                                |
# | -------------------- | ----------------------------------- |
# | `plt.subplots(2, 2)` | 2 baris × 2 kolom (total 4 grafik)  |
# | `plt.subplots(3, 1)` | 3 baris × 1 kolom (tumpuk vertikal) |
# | `plt.subplots(1, 3)` | 1 baris × 3 kolom (sejajar)         |
