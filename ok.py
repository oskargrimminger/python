import csv

# Datenstruktur zur Speicherung der Candlestick-Daten für jede Firma
candlestick_data = {
    'MSFT': [],
    'IBM': [],
    'SBUX': [],
    'AAPL': [],
    'GSPC': []
}

# Öffne die CSV-Datei und lese die Daten
with open('stockdata.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if row['Date'].startswith('2007'):  # Filtere nach dem Jahr 2007
            # Für jede Firma die Preise in Floats umwandeln
            msft_price = float(row['MSFT'])
            ibm_price = float(row['IBM'])
            sbux_price = float(row['SBUX'])
            aapl_price = float(row['AAPL'])
            gspc_price = float(row['GSPC'])

            # Berechne die Candlestick-Daten
            data = {
                'Date': row['Date'],
                'Open': {
                    'MSFT': msft_price,  # Open ist der erste Wert des Tages
                    'IBM': ibm_price,
                    'SBUX': sbux_price,
                    'AAPL': aapl_price,
                    'GSPC': gspc_price
                },
                'High': {
                    'MSFT': msft_price,  # Da du nur einen Preis pro Tag hast, ist dieser Wert der höchste
                    'IBM': ibm_price,
                    'SBUX': sbux_price,
                    'AAPL': aapl_price,
                    'GSPC': gspc_price
                },
                'Low': {
                    'MSFT': msft_price, 
                    'IBM': ibm_price,
                    'SBUX': sbux_price,
                    'AAPL': aapl_price,
                    'GSPC': gspc_price
                },
                'Close': {
                    'MSFT': msft_price,  
                    'IBM': ibm_price,
                    'SBUX': sbux_price,
                    'AAPL': aapl_price,
                    'GSPC': gspc_price
                }
            }

            candlestick_data['MSFT'].append(data)
            candlestick_data['IBM'].append(data)
            candlestick_data['SBUX'].append(data)
            candlestick_data['AAPL'].append(data)
            candlestick_data['GSPC'].append(data)

# Gib die Candlestick-Daten für jede Firma aus
for company, data in candlestick_data.items():
    print(f"--- {company} ---")
    for item in data:
        print(item)

