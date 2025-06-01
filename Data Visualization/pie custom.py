import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [120, 80, 60, 40]
}
df = pd.DataFrame(data)

# Warna kustom
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.figure(figsize=(6, 6))
plt.pie(
    df['Sales'],
    labels=df['Product'],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'black'}
)
plt.title('Product Sales Distribution', fontsize=14, fontweight='bold')
plt.axis('equal')  # Circle
plt.tight_layout()
plt.show()