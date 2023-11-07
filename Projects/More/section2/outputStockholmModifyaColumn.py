import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('stockholm.csv')

# Divide the values in the 'TG' column by 10
df['TG'] = df['TG'] / 10

# Save the updated data to a new CSV file
df.to_csv('stockholm_updated.csv', index=False)

print('Values in the TG column divided by 10 and saved to stockholm_updated.csv')
