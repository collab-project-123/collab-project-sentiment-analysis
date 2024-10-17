from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/nifty_it_news')

# Select the database and collection
db = client['nifty_it_news']
collection = db['news_collection']

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



# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])


import matplotlib.pyplot as plt
import seaborn as sns

# Count mentions of each company
company_counts = data['Company'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=company_counts.index, y=company_counts.values, palette='viridis')
plt.title('Number of Mentions per Company')
plt.xlabel('Company')
plt.ylabel('Number of Mentions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Count articles by date
articles_per_date = data['Date'].value_counts().sort_index()

# Create a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=articles_per_date.index, y=articles_per_date.values, marker='o')
plt.title('Number of News Articles Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


