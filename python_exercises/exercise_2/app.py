from functions import calcula_media_puntuaciones
from data import grupos

if __name__ == '__main__':
	print('------- Block A -------\n')
	print(calcula_media_puntuaciones(grupos))
	print('\n\n\n------- Block B -------\n')
	print(calcula_media_puntuaciones(grupos, ag="Los Yesterday"))
	print('\n\n\n------- Block C -------\n')
	print(calcula_media_puntuaciones(grupos, ag="Los Yesterday", fase="final"))
	print('\n\n\n------- Block D -------\n')
	print(calcula_media_puntuaciones(grupos, 9.876, 9.944, ag="Los Yesterday", fase="final"))

	# print(help(calcula_media_puntuaciones))
