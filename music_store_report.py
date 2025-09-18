import pandas as pd
import os

# Set data directory
DATA_DIR = 'music store data'

# Load CSV files
customer_df = pd.read_csv(os.path.join(DATA_DIR, 'customer.csv'))
invoice_df = pd.read_csv(os.path.join(DATA_DIR, 'invoice.csv'))
invoice_line_df = pd.read_csv(os.path.join(DATA_DIR, 'invoice_line.csv'))
genre_df = pd.read_csv(os.path.join(DATA_DIR, 'genre.csv'))
track_df = pd.read_csv(os.path.join(DATA_DIR, 'track.csv'))
def to_snake_case(df):
	df.columns = [col.strip().replace(' ', '_').replace('-', '_').lower() for col in df.columns]
	return df

def fix_id_columns(df):
	df.columns = [col.replace('id', '_id') if col.endswith('id') and not col.endswith('_id') else col for col in df.columns]
	return df

customer_df = to_snake_case(customer_df)
invoice_df = to_snake_case(invoice_df)
invoice_line_df = to_snake_case(invoice_line_df)
genre_df = to_snake_case(genre_df)
track_df = to_snake_case(track_df)

customer_df = fix_id_columns(customer_df)
invoice_df = fix_id_columns(invoice_df)
invoice_line_df = fix_id_columns(invoice_line_df)
genre_df = fix_id_columns(genre_df)
track_df = fix_id_columns(track_df)

# 1. Country with the most customers
country_counts = customer_df['country'].value_counts()
top_country = country_counts.idxmax()
top_country_count = country_counts.max()

# 2. Customer who spent the most money
customer_invoice = pd.merge(invoice_df, customer_df, left_on='customer_id', right_on='customer_id')
customer_spending = customer_invoice.groupby(['customer_id', 'first_name', 'last_name'])['total'].sum().reset_index()
top_customer = customer_spending.sort_values('total', ascending=False).iloc[0]

# 3. Revenue by music genre
invoice_line_track = pd.merge(
	invoice_line_df, track_df, left_on='track_id', right_on='track_id', suffixes=('', '_track')
)
invoice_line_track_genre = pd.merge(
	invoice_line_track, genre_df, left_on='genre_id', right_on='genre_id', suffixes=('', '_genre')
)
# Use 'name_genre' for genre name
genre_revenue = invoice_line_track_genre.groupby('name_genre')['unit_price'].sum().reset_index().sort_values('unit_price', ascending=False)

# 4. Average transaction value per customer
avg_transaction = customer_spending['total'].mean()

# 5. Total revenue per year
invoice_df['invoice_date'] = pd.to_datetime(invoice_df['invoice_date'])
invoice_df['year'] = invoice_df['invoice_date'].dt.year
yearly_revenue = invoice_df.groupby('year')['total'].sum().reset_index()

# Print results
print('Country with most customers:', top_country, f'({top_country_count})')
print('Top customer:', top_customer['first_name'], top_customer['last_name'], f'- ${top_customer["total"]:.2f}')
print('\nRevenue by Genre:')
print(genre_revenue)
print('\nAverage transaction value per customer: $%.2f' % avg_transaction)
print('\nTotal revenue per year:')
print(yearly_revenue)
