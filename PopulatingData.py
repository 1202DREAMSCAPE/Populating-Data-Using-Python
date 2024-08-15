import pandas as pd
import numpy as np

# Load the original data to get the headers and any potential values for columns
file_path = 'Raw.xlsx'  # Make sure this file is in the same folder as this script
df = pd.read_excel(file_path)

# Define the number of synthetic rows to generate
num_rows = 10000

# Define a helper function to generate synthetic data
def generate_data(column_name):
    if column_name in df.columns and not df[column_name].dropna().empty:
        if df[column_name].dtype == 'object':
            return np.random.choice(df[column_name].dropna().unique(), num_rows)
        elif np.issubdtype(df[column_name].dtype, np.number):
            return np.random.randint(df[column_name].min(), df[column_name].max(), num_rows)
    else:
        return [np.nan] * num_rows

# Handle date columns ensuring the relationship between them
reg_date = pd.to_datetime(np.random.choice(pd.date_range(start='2020-01-01', end='2023-01-01'), num_rows))
status_date = reg_date + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')
audit_date = status_date + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')

# Predefined values for event_cd, opportunity_cd, product_cd if not found in the data
event_codes = ['E01', 'E02', 'E03', 'E04']
opportunity_codes = ['O01', 'O02', 'O03', 'O04']
product_codes = ['P01', 'P02', 'P03', 'P04']

# Generating synthetic data based on the detected headers
synthetic_data = pd.DataFrame()

for column in df.columns:
    if column in ['audit_date', 'status_date', 'reg_date']:
        continue  # We'll handle these separately
    elif column == 'event_cd':
        synthetic_data[column] = np.random.choice(event_codes, num_rows)
    elif column == 'opportunity_cd':
        synthetic_data[column] = np.random.choice(opportunity_codes, num_rows)
    elif column == 'product_cd':
        synthetic_data[column] = np.random.choice(product_codes, num_rows)
    else:
        synthetic_data[column] = generate_data(column)

# Add the date columns after handling relationships
synthetic_data['reg_date'] = reg_date
synthetic_data['status_date'] = status_date
synthetic_data['audit_date'] = audit_date

# Save the synthetic data to an Excel file
synthetic_data.to_excel('Synthetic_Data_10000.xlsx', index=False)

print("Synthetic data with connected dates and detected headers has been generated and saved.")
