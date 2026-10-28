def req_data(message, default):
	if message == "":
		return default
	else:
		return message

if __name__ == '__main__':
	data = input('Introduce a data: ')

	print(req_data(data, 'Data not introduced'))
