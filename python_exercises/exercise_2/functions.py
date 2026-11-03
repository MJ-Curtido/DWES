def score_round(score):
	return round(score, 2)

def calcula_media_puntuaciones(grupos, *puntuaciones_extra, ag=None, fase=None):
	"""
	Esta función calcula las puntuaciones de los grupos de carnavales.
		Args:
			- grupos (dict): diccionario con modalidades, grupos y fases de las comparsas.
			- *puntuaciones_extra: 
			- ag (string): Cadena con el nombre del grupo para realizar un filtrado por dicho nombre.
			- fase (string): Cadena con la fase que se desea para al realizar la media de notas, solo cuente de dicha fase.
		Returns:
			- result (dict): diccionario con misma estrucura que grupos pero con las medias de puntuaciones calculadas.
	"""

	result = {}

	for modality, teams in grupos.items():
		""" Creo un diccionario vacío que rellenaré de los equipos filtrados según si ha introducido 'ag' o no. """
		teams_filtered = {}

		if ag: teams_filtered = dict(filter(lambda t: t[0] == ag, teams.items()))
		else: teams_filtered = teams
		
		""" Compruebo que haya algún equipo para no poner información innecesaria en el resultado. """
		if len(teams_filtered) > 0:
			result[modality] = {}

			for team, parts in teams_filtered.items():
				""" Mismo procedimiento para 'fases' que para 'ag' """
				parts_filtered = {}

				if fase: parts_filtered = dict(filter(lambda p: p[0] == fase, parts.items()))
				else: parts_filtered = parts

				if len(parts_filtered) > 0:
					score_parts = []

					for part, scores in parts_filtered.items():
						scores_rounded = list(map(score_round, scores))

						if puntuaciones_extra and fase and ag:
							scores_rounded.extend(puntuaciones_extra)

						avg = sum(scores_rounded) / len(scores_rounded)

						score_parts.append(avg)
					
					avg = score_round(sum(score_parts) / len(score_parts))
					
					result[modality][team] = avg
	
	return result

