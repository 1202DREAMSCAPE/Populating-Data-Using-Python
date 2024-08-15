import pandas as pd
import numpy as np

# Function to get user input for number of rows or generate a random number
def get_num_rows():
    choice = input("Do you want to define the number of rows? (yes/no/random): ").strip().lower()
    if choice == 'yes':
        num_rows = int(input("Enter the number of rows: "))
    elif choice == 'random':
        num_rows = np.random.randint(1000, 10000)
    else:
        num_rows = 10000  # default
    return num_rows

# Function to get user input for date range or generate a random range
def get_date_range():
    choice = input("Do you want to define the date range? (yes/no/random): ").strip().lower()
    if choice == 'yes':
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
    elif choice == 'random':
        start_date = np.random.choice(pd.date_range(start='2018-01-01', end='2020-01-01'))
        end_date = np.random.choice(pd.date_range(start='2023-01-01', end='2025-01-01'))
    else:
        start_date = '2020-01-01'  # default start date
        end_date = '2023-01-01'    # default end date
    return start_date, end_date

# Getting user input
num_rows = get_num_rows()
start_date, end_date = get_date_range()

# Define the helper functions for generating data
def generate_sales_amount(forecast_month):
    # Example seasonality effect: higher sales in December, lower in January
    if forecast_month == 12:  # December
        return np.random.normal(8000, 2000)
    elif forecast_month == 1:  # January
        return np.random.normal(2000, 1000)
    elif forecast_month in [6, 7, 8]:  # Summer months
        return np.random.normal(5000, 1500)
    else:
        return np.random.normal(4000, 1000)

def apply_environmental_factor(sales_amount):
    if np.random.rand() > 0.95:  # Introduce a rare event that decreases sales
        return sales_amount * np.random.uniform(0.5, 0.7)
    elif np.random.rand() > 0.9:  # Introduce a rare event that increases sales
        return sales_amount * np.random.uniform(1.2, 1.5)
    else:
        return sales_amount

def occasional_peaks_drops(sales_amount):
    if np.random.rand() > 0.98:  # Occasional drop
        return sales_amount * 0.5
    elif np.random.rand() > 0.98:  # Occasional peak
        return sales_amount * 1.5
    else:
        return sales_amount

def generate_sales_data(forecast_month):
    # Base sales amount with a seasonal trend
    base_sales = generate_sales_amount(forecast_month)
    # Apply environmental factors
    adjusted_sales = apply_environmental_factor(base_sales)
    # Apply occasional peaks or drops
    final_sales = occasional_peaks_drops(adjusted_sales)
    return final_sales

# Generating synthetic dates and sales data
reg_date = pd.to_datetime(np.random.choice(pd.date_range(start=start_date, end=end_date), num_rows))
status_date = reg_date + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')
audit_date = status_date + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')

# Predefined values for event_cd, opportunity_cd, product_cd if not found in the data
event_codes = ['E01', 'E02', 'E03', 'E04']
opportunity_codes = ['O01', 'O02', 'O03', 'O04']
product_codes = ['P01', 'P02', 'P03', 'P04']

# Creating synthetic data
synthetic_data = pd.DataFrame()

# Assuming headers of the original data
columns = ['event_cd', 'opportunity_cd', 'product_cd', 'forecast_month', 'forecast_amount', 'reg_date', 'status_date', 'audit_date']

for column in columns:
    if column in ['audit_date', 'status_date', 'reg_date']:
        continue  # We'll handle these separately
    elif column == 'event_cd':
        synthetic_data[column] = np.random.choice(event_codes, num_rows)
    elif column == 'opportunity_cd':
        synthetic_data[column] = np.random.choice(opportunity_codes, num_rows)
    elif column == 'product_cd':
        synthetic_data[column] = np.random.choice(product_codes, num_rows)
    elif column == 'forecast_month':
        synthetic_data[column] = pd.Series(reg_date).dt.month
    else:
        synthetic_data[column] = synthetic_data['forecast_month'].apply(generate_sales_data)

# Add the date columns after handling relationships
synthetic_data['reg_date'] = reg_date
synthetic_data['status_date'] = status_date
synthetic_data['audit_date'] = audit_date

# Save the synthetic data to an Excel file
synthetic_data.to_excel('Synthetic2.xlsx', index=False)

print("Synthetic data with connected dates, sales variability, and user-defined parameters has been generated and saved.")
