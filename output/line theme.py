import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [120, 80, 60, 40]
}

df = pd.DataFrame(data)

themes = 'seaborn-v0_8'


plt.style.use(themes)
plt.figure(figsize=(9,6))
plt.plot(df['Product'], df['Sales'], marker='o', color="#992828")
plt.title(f'\nLine Chart Style {themes}\n', fontsize=20, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Sales')

# Y-axis range
plt.ylim(0, max(df['Sales']) + 20)

# Add value labels on each point
for i in range(len(df)):
    plt.text(df['Product'][i], df['Sales'][i] + 1, str(df['Sales'][i]), ha='center')

plt.tight_layout()
plt.savefig('output/line_theme.jpg', dpi=300)
plt.show()