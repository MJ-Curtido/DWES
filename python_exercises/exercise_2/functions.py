def score_round(score):
	return round(score, 2)

def calcula_media_puntuaciones(grupos: dict, *puntuaciones_extra: tuple, ag: str or None =None, fase: str or None =None) -> dict:
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
			""" Creamos en el diccionario de resultado, la modalidad de la que hay puntuaciones. """
			result[modality] = {}

			for team, phases in teams_filtered.items():
				""" Mismo procedimiento para 'fases' que para 'ag' """
				phases_filtered = {}

				if fase: phases_filtered = dict(filter(lambda p: p[0] == fase, phases.items()))
				else: phases_filtered = phases

				if len(phases_filtered) > 0:
					score_phases = []

					for phase, scores in phases_filtered.items():
						""" Mediante un map obtengo las puntuaciones individuales redondeadas, para luego calcular la media de cada fase. """
						scores_rounded = list(map(score_round, scores))

						""" Compruebo si se han introducido puntuaciones extras para añadirlos a las puntuaciones. """
						if puntuaciones_extra and fase and ag:
							scores_rounded.extend(puntuaciones_extra)

						avg = sum(scores_rounded) / len(scores_rounded)

						score_phases.append(avg)
					
					avg = score_round(sum(score_phases) / len(score_phases))
					
					""" Creamos la agrupación con la media de puntuación dentro de la modalidad creada anteriormente. """
					result[modality][team] = avg
	
	return result

