from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/nifty_it_news')

# Select the database and collection
db = client['nifty_it_news']
collection = db['sales_data']

# Retrieve data from MongoDB
cursor = collection.find()

# Convert the cursor to a DataFrame
data = pd.DataFrame(list(cursor))

# Optionally, drop the MongoDB default '_id' field if you don't need it
data.drop('_id', axis=1, inplace=True)

# Display the DataFrame
print(data.head())

import pandas as pd

# Assuming df is your DataFrame
print(type(data))


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace this with your actual DataFrame)


df = pd.DataFrame(data)

# Convert 'Quarter' to datetime for better plotting
df['Quarter'] = pd.to_datetime(df['Quarter'], format='%b-%y')

# 1. Line Plot of Nifty Close Prices Over Quarters
plt.figure(figsize=(10, 5))
plt.plot(df['Quarter'], df['Close'], marker='o', label='Close Price', color='blue')
plt.title('Nifty Close Prices Over Quarters')
plt.xlabel('Quarter')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.show()

# 2. Bar Plot of Net Sales by Quarter
plt.figure(figsize=(10, 5))
sns.barplot(x='Quarter', y='Nifty net sales', data=df, palette='viridis')
plt.title('Nifty Net Sales by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.show()

# 3. Heatmap of Change in Profits for TCS, Infosys, and HCL
profit_data = df[['TCS change_profit', 'Infosys change_profit', 'HCL change_profit']].copy()
profit_data.fillna(0, inplace=True)  # Fill NaN with 0 for heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(profit_data, annot=True, cmap='coolwarm', cbar=True, fmt='.2f', linewidths=.5)
plt.title('Change in Profits for TCS, Infosys, and HCL')
plt.ylabel('Quarter')
plt.xlabel('Companies')
plt.show()

# 4. Scatter Plot of Nifty Change Close vs. Net Sales
plt.figure(figsize=(10, 5))
plt.scatter(df['Nifty change_close'], df['Nifty net sales'], color='orange')
plt.title('Nifty Change Close vs. Net Sales')
plt.xlabel('Nifty Change Close')
plt.ylabel('Nifty Net Sales')
plt.grid()
plt.show()
