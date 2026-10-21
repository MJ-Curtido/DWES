try:
	text = input('Introduce a long sentence: ')
	startIndex = int(input('Introduce the start index: '))
	endIndex = int(input('Introduce the end index: '))

	if startIndex > endIndex: raise type("valueException", (Exception,), {})("End index can't be higher than start index.")
	if startIndex > len(text) or endIndex > len(text): raise type("valueException", (Exception,), {})("Index can't be higher than the sentence.")

	
except Exception as e:
	print(e)
