# Import necessary libaries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the samplesuperstore dataset
data=pd.read_csv("SampleSuperstore.csv")

# pip install seaborn
# pip install matplotlib
# pip install pandas

category_sales = data.groupby('Category')['Sales'].sum()


plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()



region_profit = data.groupby('Region')['Profit'].sum()


plt.figure(figsize=(8, 6))
region_profit.plot(kind='bar', color='yellow')
plt.title('Total Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()



plt.figure(figsize=(8, 6))
plt.scatter(data['Discount'], data['Profit'], alpha=0.7, color='purple')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


plt.figure(figsize=(8, 6))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'salmon'])
plt.title('Proportion of Sales by Category')
plt.ylabel('') 
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Profit', data=data, palette='pastel')
plt.title('Profit Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


plt.figure(figsize=(8, 6))
plt.plot(category_sales.index, category_sales.values, marker='o', color='blue', linestyle='-')
plt.title('Total Sales by Category (Line Graph)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()