from pprint import pprint

from functions import calcula_media_puntuaciones
from data import grupos

if __name__ == '__main__':
	print('------- Block A -------\n')
	pprint(calcula_media_puntuaciones(grupos))
	print('\n\n\n------- Block B -------\n')
	pprint(calcula_media_puntuaciones(grupos, ag="Los Yesterday"))
	print('\n\n\n------- Block C -------\n')
	pprint(calcula_media_puntuaciones(grupos, fase="final"))
	print('\n\n\n------- Block D -------\n')
	pprint(calcula_media_puntuaciones(grupos, 9.876, 9.944, ag="Los Yesterday", fase="final"))

	# print(help(calcula_media_puntuaciones))
