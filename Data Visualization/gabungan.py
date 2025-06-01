import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV
df = pd.read_csv('data/data.csv')

# --- Bar Chart ---
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(6,4))
plt.bar(df['product'], df['sales'], color='skyblue', edgecolor='black')
plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# --- Pie Chart ---
plt.figure(figsize=(6,6))
plt.pie(df['sales'], labels=df['product'], autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution (Pie)')
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()

# --- Scatter Plot ---
plt.figure(figsize=(7,5))
scatter = plt.scatter(
    df['ad_cost'], 
    df['sales'], 
    s=df['reach']/10, 
    c=df['reach'], 
    cmap='viridis', 
    alpha=0.7,
    edgecolor='black'
)

for i, row in df.iterrows():
    plt.text(row['ad_cost'] + 30, row['sales'] + 2, row['product'], fontsize=9)

plt.colorbar(scatter, label='Ad Reach')
plt.title('Sales vs Advertising Cost with Reach Bubble')
plt.xlabel('Advertising Cost ($)')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.show()