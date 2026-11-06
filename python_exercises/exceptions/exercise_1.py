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

search_file()
