# import libraries

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# defining a scope
scope = ["https://spreadsheets.google.com/feeds", 
"https://www.googleapis.com/auth/drive"]

# load the credentials

creds = Credentials.from_service_account_file("credencials.json", scopes=scope)

# authorizing the credentials

client = gspread.authorize(creds)
sheet = client.open("e-commerce").sheet1

#extract all data

data = sheet.get_all_records()

# converting in dataframe
df = pd.DataFrame(data)

# you can do all transformations you want.

# revenue per product

df['total_revenue'] = df['unit_sales'] * df['unit_price']

# group by city and product
revenue_by_city_product = df.groupby(['city', 'product'])['total_revenue'].sum().reset_index()

# show results
print(revenue_by_city_product)


