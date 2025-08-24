import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# My first steps in data science  
print("Hello Data World! 👋")
print("I am learning to decode information into basic data and recode it...")

# Creating a simple dataset to practice
data = {
    'Month': ['settembre', 'ottobre', 'novembre', 'dicembre'],
    'Learning_Hours': [20, 25, 30, 35],
    'Confidence_Level': [3, 4, 5, 6]
       }

df = pd.DataFrame(data)
print("My Learning Journey:")
print(df)

# Simple visualization of my learning progress
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Learning_Hours'], marker='o', linewidth=2, label='Hours Studied', color='#2E86AB')
plt.plot(df['Month'], df['Confidence_Level']*5, marker='s', linewidth=2, label='Confidence (scaled)', color='#A23B72')

plt.title('My Data Science Learning Journey', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Progress', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Add some styling
plt.tight_layout()
plt.show()