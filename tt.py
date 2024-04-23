import  pandas as pd

import numpy as np  # for numerical data creation

# Create a sample DataFrame with different data types
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 28, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "HasPet": [True, False, None, True]  # None represents missing data
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)
