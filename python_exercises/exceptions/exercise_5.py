""" Se ejecuta el finally siempre porque es su función, aunque falle o no, siempre se ejecuta. """
def search_file():
	while True:
		path = input('\nIntroduce a file path:')

		if path == 'exit':
			break

		print('\n')

		try:
			with open(path) as f:
				for i in range(3):
					line = f.readline()

					if not line:
						break

					print(f'{line}')

		except FileNotFoundError:
			print('Archivo no encontrado.')	
		except Exception as e:
			print(e)
		else:
			f.close()
		finally:
			print('Esto ocurre aunque falle, porque está en el finally.')

search_file()
