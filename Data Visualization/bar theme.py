import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [120, 80, 60, 40]
}

df = pd.DataFrame(data)

themes = ['ggplot', 'seaborn-v0_8', 'fivethirtyeight', 'bmh']

for style in themes:
    plt.style.use(style)
    plt.figure(figsize=(6,4))
    plt.bar(df['Product'], df['Sales'], color='skyblue', edgecolor='black')
    plt.title(f'Product sales - Style {style}', fontsize=12, fontweight='bold')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.show()