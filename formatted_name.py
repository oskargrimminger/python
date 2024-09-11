def get_formatted_name(frist_name, middle_name, last_name):
	'''display full name'''
	if middle_name:
		full_name = 'frist_name' + 'middle_name' + 'last_name'
	else:
		full_name = 'frist_name' + '' + 'last_name'
		
get_formatted_name('oskar' , 'grimminger')