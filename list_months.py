
list_Jan = []
list_Feb = []
list_Mar = []
list_Apr = []
list_May = []
list_Jun = []
list_Jul = []
list_Aug = []
list_Sep = []
list_Okt = []
list_Nov = []
list_Dec = []

    for row in csv_reader:
    	month = datetime.strptime(row['Date'], '%m') 
    	if '%m' == '01':
    		list_Jan.append(month)
    	elif '%m' == '02':
    		list_Feb.append(month)
    	elif '%m' == '03':
    		list_Mar.append(month)
    	elif '%m' == '04':
    		list_Apr.append(month)
    	elif '%m' == '05':
    		list_May.append(month)
    	elif '%m' == '06':
    		list_Jun.append(month)
    	elif '%m' == '07':
    		list_Jul.append(month)
    	elif '%m' == '08':
    		list_Aug.append(month)
    	elif '%m' == '09':
    		list_Sep.append(month)
    	elif '%m' == '10':
    		list_Okt.append(month)
    	elif '%m' == '11':
    		list_Nov.append(month)
    	elif '%m' == '02':
    		list_Dec.append(month)
    