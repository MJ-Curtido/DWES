def average(list_data):
	sumatory = 0

	for e in list_data:
		sumatory += e
	
	return round(sumatory / len(list_data), 2)

def limits(list_data):
	minimum = list_data[0]
	maximum = list_data[0]

	for e in list_data:
		if e < minimum: minimum = e
		if e > maximum: maximum = e
	
	return minimum, maximum
