import pandas as pd

df = pd.read_csv("sample.csv")
print(df.head())

high_rated= df[df['rating']>4]
print(high_rated)

# Sorting
sorted_df = df.sort_values(by="price") #ascending
print(sorted_df)

sorted_df = df.sort_values(by="price",ascending=False) #descending
print(sorted_df)

# Add New Column
df['price_usd']=df["price"]*1.25
print(df)

## Average
print("Average Price: ",df['price'].mean())
print("Average Rating: ",df['rating'].mean())
## filter book wihich price is less than 25

filtered= df[df['price']<20]
print(filtered)

# Create another csv and export to file
filtered.to_csv('under_twenty.csv',index=False)