from fredapi import Fred
import pandas as pd

fred = Fred(api_key='844be8eed376f771029fd065ff2049b7')

# Get daily SOFR rates for the last 500 days
sofr_data = fred.get_series('SOFR', observation_start='2022-01-01')

# Convert to DataFrame
sofr_df = pd.DataFrame(sofr_data, columns=['Rate'])

# Remove rows with missing SOFR rates
sofr_df.dropna(subset=['Rate'], inplace=True)

# Filter for last 500 days
sofr_df = sofr_df.tail(500)

# Export to CSV
sofr_df.to_csv('/Users/thomas/Classes/PACE Classes/Advanced Investment Management/Project 1/SOFR_last_500_days.csv', index_label='Date')

# Display data
print(sofr_df)