
import csv
from datetime import datetime


monthly_data = {
    'January': [],
    'February': [],
    'March': [],
    'April': [],
    'May': [],
    'June': [],
    'July': [],
    'August': [],
    'September': [],
    'October': [],
    'November': [],
    'December': []
}

with open('stockdata.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:   	
    	date = datetime.strptime(row['Date'], '%Y-%m-%d')
    	if date.year == 2007:
            data = {
                'MSFT': float(row['MSFT']),
                'IBM': float(row['IBM']),
                'SBUX': float(row['SBUX']),
                'AAPL': float(row['AAPL']),
                'GSPC': float(row['GSPC']),
                'Date': row['Date']
            }

            if date.month == 1:
                monthly_data['January'].append(data)
            elif date.month == 2:
                monthly_data['February'].append(data)
            elif date.month == 3:
                monthly_data['March'].append(data)
            elif date.month == 4:
                monthly_data['April'].append(data)
            elif date.month == 5:
                monthly_data['May'].append(data)
            elif date.month == 6:
                monthly_data['June'].append(data)
            elif date.month == 7:
                monthly_data['July'].append(data)
            elif date.month == 8:
                monthly_data['August'].append(data)
            elif date.month == 9:
                monthly_data['September'].append(data)
            elif date.month == 10:
                monthly_data['October'].append(data)
            elif date.month == 11:
                monthly_data['November'].append(data)
            elif date.month == 12:
                monthly_data['December'].append(data)

def calculate_candlestick(data, company):
    if len(data) == 0:
        return None
    
    open_price = data[0][company]
    close_price = data[-1][company]
    high_price = max([entry[company] for entry in data])
    low_price = min([entry[company] for entry in data])
    
    return {
        'Open': open_price,
        'Close': close_price,
        'High': high_price,
        'Low': low_price
    }

for month, data in monthly_data.items():
    print(f"Candlestick data for {month}:")
    for company in ['MSFT', 'IBM', 'SBUX', 'AAPL', 'GSPC']:
        candlestick = calculate_candlestick(data, company)
        if candlestick:
            print(f"{company}: {candlestick}")
    print("\n")

