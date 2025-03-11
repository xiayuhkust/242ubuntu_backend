import pandas as pd
import os

# Create a sample Excel file with Twitter URLs
data = {
    'Name': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Twitter': ['https://twitter.com/elonmusk', 'https://twitter.com/BillGates', 
                'https://x.com/satyanadella', 'https://twitter.com/sundarpichai', 
                'https://x.com/tim_cook']
}

# Create directory if it doesn't exist
os.makedirs('test_data', exist_ok=True)

# Create DataFrame and save to Excel
df = pd.DataFrame(data)
output_path = os.path.join('test_data', 'sample_twitter_urls.xlsx')
df.to_excel(output_path, index=False)
print(f'Created sample Excel file at {output_path}')
