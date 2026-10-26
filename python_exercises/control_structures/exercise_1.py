try:
	mark = int(input('Introduce an integer mark (0-10): '))
	if mark < 0 or mark > 10: raise type("IndexError", (Exception,), {})("Introduce a valid mark.")

#	if mark < 5:
#		print('Insuficiente')
#	elif 5 <= mark <= 6:
#		print('Suficiente')
#	elif mark == 7:
#		print('Bien')
#	elif (8 <= mark <= 9:
#		print('Notable')
#	elif mark == 10:
#		print('Sobresaliente')
#	else:
#		print('Introduce a valid mark.')

	print('Insuficiente') if mark < 5 else print('Suficiente') if 5 <= mark <= 6 else print('Bien') if mark == 7 else print('Notable') if 8 <= mark <= 9 else print('Sobresaliente') if mark == 10 else print('Introduce a valid mark.')

except ValueError:
	print("Error: Caracter introduced wasn't a number.")
except Exception as e:
	print(e)
