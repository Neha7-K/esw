import pandas as pd

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Leaf Temperature': [27.4, 27, 26.3, 26.9, 28, 28.6, 27.2, 27.1, 27.3, 27.8, 28, 28.2, 27.6, 27.2],
    'Air temperature': [27.56, 27.9, 27.76, 26.7, 26.8, 26.37, 26.47, 27, 26.14, 27.2, 26.11, 27, 26.14, 23.9],
    'Soil Moisture': [14.3, 14.7, 15.3, 15.5, 15.9, 13.4, 16.8, 18, 17.2, 16.4, 15.8, 14.7, 14.2, 17.4],
    'pH': [5.17, 5.5, 5.78, 5.02, 4.67, 4.82, 5.23, 5.46, 5.36, 5.18, 5.17, 4.82, 5.34, 5.17]
}

df = pd.DataFrame(data)

correlation_coefficient = df['Leaf Temperature'].corr(df['Air temperature'])

# Normalize Leaf Temperature
df['Normalized Leaf Temperature'] = df['Leaf Temperature'] - correlation_coefficient * df['Air temperature']

print("Normalized DataFrame:")
print(df[['Day', 'Leaf Temperature', 'Air temperature', 'Normalized Leaf Temperature']])
