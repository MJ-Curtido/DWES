countWords = {}

while True:
	text = input('Introduce a sentence: ')

	words = text.split()

	for word in words:
		if countWords.get(word, 0) > 0:
			countWords[word] += 1
		else:
			countWords[word] = 1
	if text == "":
		break

for key, value in countWords.items():
	print(f'- {key}: {value}')
