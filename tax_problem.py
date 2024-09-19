import math

def round_up(value ):
	return math.ceil(value/0.05) * 0.05

def calculate_tax(price, rate):
    tax = (rate / 100) * price
    return round_up(tax)

def process_item(name, price,imported,exempt):
	tax = 0
	if not exempt:
		tax += calculate_tax(price, 10)
	if imported:
		tax += calculate_tax(price, 5)

	total_price = price + tax 
	return tax, total_price

def print_receipt(items):
    total_tax = 0
    total_cost = 0


    print('Receipt')
    for item in items:
    	name, price, imported,exempt = item
    	tax, total_price = process_item(name, price, imported, exempt)
    	total_tax += tax
    	total_cost += total_price
    	print(f"{name}: ${total_price:.2f} (Tax: ${tax:.2f})")

    print(f"Total Sales Taxes: ${total_tax:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")



items = [

	("book", 12.49, False, True),          
    ("music CD", 14.99, False, False),    
    ("chocolate bar", 0.85, False, True)  
]

print_receipt(items)  




