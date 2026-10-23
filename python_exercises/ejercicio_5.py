try:
	text = input('Introduce a long sentence: ')

	startIndex = int(input('Introduce the start index: ')) - 1
	if startIndex < 0: raise type("valueException", (Exception,), {})("Index can't be 0 or negative.")
	endIndex = int(input('Introduce the end index: '))
	if endIndex < 0: raise type("valueException", (Exception,), {})("Index can't be 0 or negative.")

	if startIndex > endIndex: raise type("valueException", (Exception,), {})("End index can't be higher than start index.")
	if startIndex > len(text) or endIndex > len(text): raise type("valueException", (Exception,), {})("Index can't be higher than the sentence.")

	print(text[startIndex:endIndex])
except Exception as e:
	print(e)
