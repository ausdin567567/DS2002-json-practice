import json
import pandas as pd

# Step 2
data_path = '/Users/ausdinrahman/Downloads/schacon.repos.json'  
with open(data_path, 'r') as file:
    data = json.load(file)

# Step 3i/3ii: Getting the fields
extracted_fields = []
for field in data[:5]:  #1st five lines 
    extracted_fields.append([
        field['name'],
        field['html_url'],
        field['updated_at'],
        field['visibility']
    ])

# Step 3iii: Dictionary entry to then a pandas dataframe entry
csv_path = '/Users/ausdinrahman/Downloads/chacon.csv'
df = pd.DataFrame(extracted_fields, columns=['name', 'html_url', 'updated_at', 'visibility'])
df.to_csv(csv_path, index=False, header=False)