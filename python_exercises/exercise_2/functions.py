def calcula_media_puntuaciones(grupos, *puntuaciones_extra, ag=None, fase=None):
	result = {}
	# TODO: Hacer una copia del array que me viene, y realizar filtros (con filter()) para controlar los parámetros ag y fase dentro del for global

	if puntuaciones_extra:
		print('Entra')
	else:
		for modality, teams in grupos.items():
			result[modality] = {}
			
			for team, parts in teams.items():
				sumatory = 0
				count = 0

				for part, scores in parts.items():
					#score: sumatory += score for score in part
					for score in scores:
						sumatory += score
						count += 1
				
				result[modality][team] = round(sumatory / count, 2)
	
	return result

