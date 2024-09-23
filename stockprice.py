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
        try:
            date = datetime.strptime(row['Date'], '%Y-%m-%d')
        except Exception:
            pass

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


def calculate_percentage_change(open_price, other_price):
    return ((other_price - open_price) / open_price) * 100


def find_greatest_change(data):
    if len(data) == 0:
        return None
    
    greatest_change = -float('inf')  
    greatest_company = None

    for company in ['MSFT', 'IBM', 'SBUX', 'AAPL', 'GSPC']:
        candlestick = calculate_candlestick(data, company)
        if candlestick:
            
            change_high = calculate_percentage_change(candlestick['Open'], candlestick['High'])
            change_low = calculate_percentage_change(candlestick['Open'], candlestick['Low'])

            
            max_change = max(change_high, abs(change_low))

        
            if max_change > greatest_change:
                greatest_change = max_change
                greatest_company = (company, max_change)

    return greatest_company


for month, data in monthly_data.items():
    print(f"Candlestick data for {month}:")    
    for company in ['MSFT', 'IBM', 'SBUX', 'AAPL', 'GSPC']:
        candlestick = calculate_candlestick(data, company)
        if candlestick:
            print(f"{company}: {candlestick}")

   
    greatest_change_company = find_greatest_change(data)

    if greatest_change_company:
        company, change = greatest_change_company
        print(f"Company with the greatest change in {month} is {company} with a change of {change:.2f}%.\n")
    else:
        print(f"No Data for this {Month}")
    
