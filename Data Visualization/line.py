import pandas as pd
import matplotlib.pyplot as plt
import os

# Sample data
data = {
    'Date': pd.date_range(start='2025-05-01', periods=7, freq='D'),
    'Units_Sold': [20, 30, 25, 35, 40, 38, 42]
}

df = pd.DataFrame(data)

os.makedirs('output', exist_ok=True)


# Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Units_Sold'], marker='o', linestyle='-', color='green')

# Title and labels
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Units Sold')

# Rotate date labels
plt.xticks(rotation=45)

# Y-axis range
plt.ylim(0, max(df['Units_Sold']) + 10)

# Add value labels on each point
for i in range(len(df)):
    plt.text(df['Date'][i], df['Units_Sold'][i] + 1, str(df['Units_Sold'][i]), ha='center')

# Save and show
plt.tight_layout()
plt.savefig('output/sales_line_chart.png')
plt.show()