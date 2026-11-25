# Examen del bloque de Python (T2): Bicis de la Campiña

**Duración: 3 horas.** Puntuación: 10 puntos (parte 1: 3 · parte 2: 2 · parte 3: 2 · requisitos técnicos: 1 · parte 4: 2).

*Bicis de la Campiña* es un pequeño servicio de alquiler de bicicletas con estaciones repartidas por Jerez. Cada alquiler se registra cuando el cliente saca la bici y se cierra al devolverla. La organización necesita un programa que calcule precios, resuma la actividad del día y guarde un informe.

## Normas

- Trabaja **solo en este repositorio**. Haz *commit* y *push* con frecuencia para no perder trabajo, pero **un push no es una entrega**.
- **Para entregar**, sube una etiqueta `submit/` con un número nuevo cada vez:

  ```bash
  git push
  git tag submit/1              # la siguiente entrega: submit/2, submit/3…
  git push origin submit/1
  ```

  Se califica **la última entrega anterior a la hora de cierre**. Sin etiqueta no hay entrega ni nota. Si Git dice que la etiqueta ya existe, usa el número siguiente. Entrega pronto y vuelve a entregar cuando avances: no lo dejes para el último minuto.
- Unos segundos después de cada entrega verás en GitHub una puntuación automática (✓/✗ junto al commit y en *Releases*). Una ✗ **no** significa que la entrega haya fallado: indica que alguna comprobación no pasa todavía. **Esa puntuación no es tu nota**: solo comprueba los mismos valores que las «Salidas esperadas» de este enunciado. La calificación se hace después del examen, con más pruebas.
- No cambies los nombres de los ficheros, funciones, clases, parámetros ni constantes que da el enunciado o el esqueleto: la corrección automática los usa.
- No modifiques las constantes ni los datos (`TARIFAS`, `EXTRAS`, `REGISTROS`, `REGISTROS_IMPORTADOS`…).
- Solo se usa la biblioteca estándar de Python: no hay que instalar nada.
- Un programa que no arranca (error de sintaxis, `import` roto) hace fallar todas las pruebas que dependen de él. **Antes de cada entrega, ejecuta `python comprobaciones.py`.**
- **Material permitido:** la documentación oficial de Python (<https://docs.python.org/es/3/>) y los apuntes del módulo.
- **No se permite** consultar la actividad de profundización ni ningún otro código tuyo o ajeno hecho antes del examen, esté en tu equipo o en GitHub.
- **No se permite** ningún tipo de asistencia en el editor: ni autocompletado, ni sugerencias, ni IA (Copilot, chats, extensiones…), ni ninguna otra herramienta de IA. El repositorio incluye `.vscode/settings.json`, que desactiva esas ayudas en VS Code: **no lo modifiques ni lo borres**. Modificarlo se considera un incumplimiento de las normas del examen.

## 1. Prepara el entorno

Clona el repositorio, entra en su carpeta y crea un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python comprobaciones.py
```

El `.gitignore` ya excluye `.venv/` e `informe.json`.

En VS Code, abre **la carpeta del repositorio** (*Archivo → Abrir carpeta…*), no ficheros sueltos, para que se apliquen los ajustes del examen de `.vscode/settings.json`.

El proyecto son tres módulos (el esqueleto ya los trae) más un fichero de comprobaciones:

```text
app.py        → programa principal (python app.py)
  ├── alquiler.py   → las clases Alquiler y AlquilerAbonado
  └── tarifas.py    → constantes, excepciones y funciones de cálculo
comprobaciones.py → reproduce las «Salidas esperadas» de este enunciado
```

`app.py` importa de los otros dos y `alquiler.py` importa de `tarifas.py`. En cambio, **`tarifas.py` no debe importar `alquiler.py`**: sus funciones trabajan con cualquier objeto que tenga `.cliente`, `.tipo`, `.estacion`, `.minutos` y `.devuelto`.

## 2. Los datos

Los datos están en `app.py`, en la lista `REGISTROS`, y tienen este formato:

```python
REGISTROS = [
    {"cliente": "Nerea Campos", "bici": "urbana",
     "estacion": "Plaza del Arenal", "minutos": 45},
    {"cliente": "Tomás Herrera", "bici": "electrica",
     "estacion": "Alameda Cristina", "minutos": 125, "abonado": True},
    {"cliente": "Irene Valle", "bici": "urbana",
     "estacion": "Estación de tren"},
    ...
]
```

Fíjate en tres detalles:

- El tipo de bici viene en la clave **`"bici"`**, pero en la clase el atributo se llama `tipo`.
- Si la bici aún no se ha devuelto (alquiler **en curso**), el registro **no tiene** la clave `"minutos"`.
- La clave `"abonado"` es opcional. Si no aparece, el cliente **no** es abonado.

Las constantes del dominio están en `tarifas.py`:

| Constante | Valor | Significado |
|---|---|---|
| `TARIFAS` | `{"urbana": 2.5, "electrica": 4.0, "infantil": 1.5}` | euros **por hora o fracción** según el tipo de bici |
| `EXTRAS` | `{"casco": 1.5, "candado": 1.0, "sillita": 2.0}` | extras: cada uno se cobra una vez por alquiler |
| `DESCUENTO_ABONADO` | `0.20` | 20 % de descuento a abonados |
| `INICIO_FERIA`, `FIN_FERIA` | `date(2027, 5, 8)`, `date(2027, 5, 15)` | semana de la Feria del Caballo |
| `RECARGO_FERIA` | `2.0` | euros que se suman si el alquiler es en feria |

## 3. Parte 1: el módulo `tarifas.py` (3 puntos)

### 3.1 Excepciones propias

El esqueleto declara la excepción base `ErrorAlquiler` y sus tres hijas. Complétalas: cada hija guarda el dato problemático en el atributo indicado, y su mensaje (lo que muestra `str(error)` o `print(error)`) debe ser **exactamente** este:

| Excepción | Atributo | Se lanza cuando... | Mensaje (ejemplo) |
|---|---|---|---|
| `TipoInvalidoError` | `tipo` | el tipo no está en `TARIFAS` | `Tipo de bici no reconocido: 'tandem'` |
| `ExtraInvalidoError` | `extra` | el extra no está en `EXTRAS` | `Extra no disponible: 'cesta'. Disponibles: casco, candado, sillita` |
| `DuracionInvalidaError` | `minutos` | una duración es cero o negativa | `La duración debe ser positiva: -5` |

Cada una se crea con el dato como único argumento: `TipoInvalidoError("tandem")`, `ExtraInvalidoError("cesta")`, `DuracionInvalidaError(-5)`.

La lista de disponibles del segundo mensaje refleja los extras que haya en `EXTRAS`, en su orden: si se añadiera un extra nuevo, aparecería sin tocar la excepción.

### 3.2 Duraciones

Tres funciones, **con anotaciones de tipos** (parámetro y retorno) y docstring. Las tres lanzan `DuracionInvalidaError` si la duración no es positiva.

- `horas_minutos(minutos)`: la tupla `(horas, minutos)`: `125` → `(2, 5)`.
- `formato_duracion(minutos)`: el texto `H:MM`, con dos dígitos en los minutos: `125` → `"2:05"`, `45` → `"0:45"`, `600` → `"10:00"`.
- `horas_facturables(minutos)`: las horas que se cobran; **cada hora empezada cuenta entera**: `45` → `1`, `60` → `1`, `61` → `2`.

### 3.3 El precio de un alquiler

`precio_alquiler` calcula lo que se cobra por un alquiler. Recibe el tipo de bici, los minutos y **cualquier número de extras** (también ninguno). Además admite `abonado` (por defecto, no es abonado) y `fecha` (por defecto, sin fecha), que **solo se pueden indicar por su nombre**. Tiene que poder llamarse así:

```python
precio_alquiler("urbana", 45)
precio_alquiler("electrica", 125, "casco", "candado")
precio_alquiler("urbana", 90, "sillita", abonado=True)
precio_alquiler("infantil", 30, fecha=date(2027, 5, 10))
precio_alquiler("electrica", 61, "casco", abonado=True, fecha=date(2027, 5, 15))
```

Reglas de cálculo, en este orden:

1. Si el tipo no existe: `TipoInvalidoError`.
2. Precio base: la tarifa del tipo por las horas facturables. Si la duración no es positiva: `DuracionInvalidaError`.
3. Se suma cada extra. Si un extra no existe: `ExtraInvalidoError`.
4. Si hay fecha y está **dentro de la feria, ambos días incluidos**, se suma `RECARGO_FERIA`.
5. Si el cliente es abonado, se aplica el descuento sobre **todo** lo anterior.
6. El resultado se devuelve **redondeado a dos decimales**. Solo se redondea el resultado final.

Puedes suponer que la fecha, si llega, es un `date` válido.

### 3.4 Resumen y ranking

Estas funciones reciben una lista de alquileres (objetos) y, opcionalmente, un tipo de bici. **Si no se indica tipo, entran todos los alquileres; si se indica, solo los de ese tipo.** No deben modificar la lista recibida.

- `resumen(alquileres, tipo=…)`: la tupla `(total, devueltos, media_min, maximo_min)`: cuántos alquileres hay en la selección, cuántos están devueltos, la media de minutos de los devueltos redondeada al minuto entero más próximo y la duración máxima de los devueltos. Puedes suponer que siempre hay al menos un devuelto.
- `ranking(alquileres, tipo=…, top=…)`: los alquileres devueltos **del más largo al más corto**. Cada puesto es un diccionario `{"pos": ..., "cliente": ..., "estacion": ..., "duracion": ...}`, con la posición desde 1 y la duración ya formateada como `H:MM`. Si se indica `top`, solo esos primeros puestos.

Llamadas de ejemplo:

```python
resumen(alquileres)
resumen(alquileres, tipo="electrica")
ranking(alquileres, tipo="urbana")
ranking(alquileres, top=1)
```

### Salida esperada de la parte 1

`python comprobaciones.py`, sección «Parte 1»:

```text
(2, 5) 2:05 0:45 10:00
1 2 1
2.5
14.5
5.6
3.5
9.2
Capturado por la base: Tipo de bici no reconocido: 'tandem'
Capturado: Extra no disponible: 'cesta'. Disponibles: casco, candado, sillita (extra='cesta')
```

`resumen` y `ranking` se comprueban en la parte 3, porque necesitan la lista de alquileres que construye `cargar_alquileres`.

## 4. Parte 2: el módulo `alquiler.py` (2 puntos)

### 4.1 La clase `Alquiler`

1. Se crea con `Alquiler(cliente, tipo, estacion, minutos)`. Si el alquiler sigue en curso, los minutos se omiten y valen `None`.
2. El **tipo** se valida al crear el alquiler y cada vez que se cambia (`alquiler.tipo = "patinete"`). Si no es válido, se lanza `TipoInvalidoError` y el alquiler conserva el tipo que tenía.
3. Los **minutos** se validan igual, al crear y al cambiar: valen `None` (en curso) o un número de minutos. Si son cero o negativos, se lanza `DuracionInvalidaError`.
4. `alquiler.devuelto` (sin paréntesis) vale `True` si el alquiler tiene minutos y `False` si no, y cambia solo si cambian los minutos. **No se puede asignar**: `alquiler.devuelto = False` lanza `AttributeError`.
5. `Alquiler.es_tipo_valido(tipo)` devuelve `True` o `False`, y se puede usar **sin crear ningún alquiler**.
6. `Alquiler.desde_registro(registro)` crea un alquiler a partir de uno de los diccionarios de `REGISTROS`. Si falta la clave `"minutos"`, el alquiler está en curso. Ignora las claves que no necesita y **no modifica** el diccionario. Llamado como `AlquilerAbonado.desde_registro(registro)`, devuelve un `AlquilerAbonado`.
7. `importe()`: lo que se cobra por el alquiler (su precio sin extras); `0.0` si sigue en curso.
8. `print(alquiler)` muestra exactamente `Cliente [tipo] — estacion (H:MM)`, o `(en curso)` si no está devuelto:
   ```text
   Nerea Campos [urbana] — Plaza del Arenal (0:45)
   Irene Valle [urbana] — Estación de tren (en curso)
   ```

### 4.2 Abonados y recaudación

Un `AlquilerAbonado` **es un** `Alquiler` (`isinstance(abonado, Alquiler)` es `True`) y se comporta igual salvo en dos cosas:

- `importe()` aplica el descuento de abonado (`0.0` si sigue en curso).
- `print(abonado)` añade la marca: `Tomás Herrera [electrica, abonado] — Alameda Cristina (2:05)`.

`recaudacion(alquileres)` suma los importes de una lista que mezcla alquileres normales y de abonados, y devuelve el total redondeado a dos decimales. Debe funcionar con **cualquier objeto que tenga un método `importe()`**, sea de la clase que sea.

### Salida esperada de la parte 2

```text
Nerea Campos [urbana] — Plaza del Arenal (0:45)
True 2.5
Irene Valle [urbana] — Estación de tren (en curso) | devuelto: False | importe: 0.0
Capturado: Tipo de bici no reconocido: 'tandem'
Capturado: La duración debe ser positiva: -5
Tomás Herrera [electrica, abonado] — Alameda Cristina (2:05)
¿Es un Alquiler? True
9.6
Recaudación: 22.10 €
```

## 5. Parte 3: el programa `app.py` (2 puntos)

### 5.1 Carga y persistencia

- `cargar_alquileres(registros)`: devuelve la lista de alquileres. Los registros con `"abonado": True` se cargan como `AlquilerAbonado`; el resto (con `"abonado": False` o sin esa clave), como `Alquiler`.
- `guardar_informe(alquileres, ruta)`: escribe en `ruta` un fichero JSON con las claves `"recaudacion"` (la recaudación total) y `"ranking"` (el ranking general). El fichero va en UTF-8, con **sangría de 2 espacios** y con las tildes **tal cual** (`"Inés"`, no `"In\u00e9s"`).

### 5.2 Entrada por teclado

- `pedir_entero(mensaje, minimo, maximo)` **ya viene hecha** en el esqueleto: muestra `mensaje (minimo-maximo): ` y repite hasta recibir un entero dentro de los límites. Úsala; no la cambies.
- `pedir_tipo()`: pide `Tipo (urbana/electrica/infantil o Intro para todos): ` y repite, avisando con `Tipo no reconocido.`, hasta recibir un tipo válido. Acepta mayúsculas y espacios alrededor (`"  Electrica "` vale como `"electrica"`). Si se pulsa Intro sin escribir nada, devuelve `None` (todos los tipos).

### 5.3 El menú

`main()` carga los alquileres de `REGISTROS`, muestra cuántos se han cargado (`Cargados 10 alquileres.` con los datos del esqueleto) y muestra este menú, que se repite hasta elegir 0:

```text
=== BICIS DE LA CAMPIÑA ===
1) Ranking de alquileres
2) Calcular precio
3) Guardar informe
0) Salir
```

La opción se lee con `pedir_entero("Opción", 0, 3)`.

| Opción | Qué hace |
|---|---|
| 1 | pide el tipo con `pedir_tipo()` y muestra cada puesto del ranking en una línea: `1. Lorena Díaz — 4:00 — Alameda Cristina` |
| 2 | pide, **en este orden**: el tipo de bici, los minutos (`pedir_entero("Minutos", 1, 1440)`), los extras uno a uno hasta un Intro en blanco (antes muestra los disponibles con su precio), si es abonado (`s`/`n`; cualquier respuesta distinta de `s` cuenta como no) y una fecha opcional `AAAA-MM-DD`. Los textos exactos de cada pregunta están en el ejemplo de sesión. **Ni el tipo ni los extras se comprueban al leerlos**: si alguno no existe, se muestra `Error: ` seguido del mensaje de la excepción y el menú continúa. Si todo es correcto, muestra el precio con dos decimales: `Precio del alquiler: 14.50 €` |
| 3 | guarda el informe en `RUTA_INFORME` y muestra `Informe guardado en informe.json` |
| 0 | muestra `¡Hasta pronto!` y termina |

Si la fecha no es una fecha válida, se muestra `Fecha no válida: se calcula sin fecha.` y se calcula el precio sin fecha.

`python app.py` arranca el programa, pero **importar cualquiera de los tres módulos no debe mostrar nada ni pedir nada**.

### Ejemplo de sesión

El menú se repite tras cada opción (aquí se omite para abreviar). Los textos y los datos deben coincidir.

```text
Cargados 10 alquileres.

=== BICIS DE LA CAMPIÑA ===
1) Ranking de alquileres
2) Calcular precio
3) Guardar informe
0) Salir
Opción (0-3): hola
Eso no es un número entero.
Opción (0-3): 1
Tipo (urbana/electrica/infantil o Intro para todos): infantil
1. Celia Navarro — 1:15 — Estación de tren
2. Pablo Serrano — 0:30 — Plaza del Arenal

Opción (0-3): 2
Tipo de bici: electrica
Minutos (1-1440): 125
Extras disponibles:
  - casco (1.50 €)
  - candado (1.00 €)
  - sillita (2.00 €)
Extra (Intro para terminar): casco
Extra (Intro para terminar): candado
Extra (Intro para terminar):
¿Abonado (s/n)? n
Fecha AAAA-MM-DD (Intro para no indicar):
Precio del alquiler: 14.50 €

Opción (0-3): 2
Tipo de bici: urbana
Minutos (1-1440): 30
Extras disponibles:
  ...
Extra (Intro para terminar): cesta
Extra (Intro para terminar):
¿Abonado (s/n)? n
Fecha AAAA-MM-DD (Intro para no indicar):
Error: Extra no disponible: 'cesta'. Disponibles: casco, candado, sillita

Opción (0-3): 3
Informe guardado en informe.json

Opción (0-3): 0
¡Hasta pronto!
```

### Salida esperada de la parte 3

`comprobaciones.py` carga los alquileres, muestra cuántos hay y la clase del segundo, dos resúmenes, el ranking urbano, el primer puesto general, y la recaudación y el número de puestos del informe guardado:

```text
10 AlquilerAbonado
(10, 8, 111, 240)
(4, 3, 142, 240)
{'pos': 1, 'cliente': 'Diego Lozano', 'estacion': 'Alameda Cristina', 'duracion': '3:10'}
{'pos': 2, 'cliente': 'Rubén Ortega', 'estacion': 'Plaza del Arenal', 'duracion': '2:00'}
{'pos': 3, 'cliente': 'Nerea Campos', 'estacion': 'Plaza del Arenal', 'duracion': '0:45'}
[{'pos': 1, 'cliente': 'Lorena Díaz', 'estacion': 'Alameda Cristina', 'duracion': '4:00'}]
51.4 8
```

## 6. Requisitos técnicos (1 punto)

Además de funcionar, la solución debe usar las siguientes técnicas del bloque de Python. Decide tú dónde tiene sentido cada una:

- excepciones propias organizadas en una jerarquía;
- una función que admite cualquier número de argumentos y parámetros que solo se pueden pasar por nombre;
- `filter` con una función con nombre, y al menos una `lambda`;
- propiedades: con validación al asignar y de solo lectura;
- un método estático, un método de clase y herencia con métodos sobrescritos;
- `match` para elegir entre varias opciones;
- `with` para trabajar con ficheros;
- anotaciones de tipos en las funciones de duraciones.

Se comprueba automáticamente que estén y, después, a mano que se usen donde tienen sentido.

## 7. Parte 4: para nota (2 puntos)

Esta parte es **independiente** de las anteriores: no cambia lo que ya funciona. Hazla al final.

### 7.1 Registros defectuosos

Los registros que llegan de otras estaciones no siempre vienen bien. En `app.py` tienes una lista de ejemplo, `REGISTROS_IMPORTADOS`.

Crea en `tarifas.py` la excepción `RegistroInvalidoError`, hija de `ErrorAlquiler`. Se crea con `RegistroInvalidoError(posicion, clave, motivo)`, guarda la posición y la clave en los atributos `posicion` y `clave`, y su mensaje es exactamente:

```text
Registro 3 (bici): falta la clave
```

Escribe en `app.py` la función `importar_registros(registros)`. Devuelve la tupla `(alquileres, errores)`:

- `alquileres`: los alquileres de los registros correctos, creados igual que en `cargar_alquileres` y en el mismo orden.
- `errores`: un `RegistroInvalidoError` por cada registro que no se puede convertir, en el orden de la lista. La importación **no se detiene** ante un registro defectuoso.

La `posicion` es el número del registro en la lista, empezando por 1. La clave y el motivo dependen del problema:

| Problema del registro | `clave` | `motivo` |
|---|---|---|
| falta `"cliente"`, `"bici"` o `"estacion"` | la clave que falta | `falta la clave` |
| el tipo de bici no existe | `bici` | el mensaje del `TipoInvalidoError` |
| los minutos no son positivos | `minutos` | el mensaje del `DuracionInvalidaError` |

Cada `RegistroInvalidoError` conserva como **causa** la excepción original que lo provocó, que se puede consultar en `error.__cause__`: el `TipoInvalidoError` o el `DuracionInvalidaError` correspondiente y, si falta una clave, el `KeyError` de esa clave. Puedes suponer que cada registro tiene como mucho un problema. La función **no modifica** ni la lista ni sus diccionarios.

### 7.2 Desempate en el ranking

Cuando dos alquileres duran lo mismo, el ranking los ordena **por cliente, en orden alfabético**.

### Salida esperada de la parte 4

`comprobaciones.py` importa `REGISTROS_IMPORTADOS`, muestra cuántos alquileres y errores salen, la clase del segundo alquiler y cada error con el nombre de su causa, y después un ranking con empates:

```text
3 3 AlquilerAbonado
Registro 2 (bici): Tipo de bici no reconocido: 'tandem' | causa: TipoInvalidoError
Registro 4 (minutos): La duración debe ser positiva: 0 | causa: DuracionInvalidaError
Registro 5 (estacion): falta la clave | causa: KeyError
1 Carla Pastor 1:30
2 Adrián Gallego 1:00
3 Marta Ibáñez 1:00
4 Yago Fuentes 1:00
```

## Criterios de corrección

La corrección automática comprueba, además de las salidas anteriores, casos que no aparecen en el enunciado (límites, errores, otras combinaciones de datos). En particular:

1. Las excepciones heredan de `ErrorAlquiler`, guardan su dato como atributo y tienen el mensaje exacto.
2. `precio_alquiler` acepta cualquier número de extras, respeta el orden de las reglas y redondea a dos decimales.
3. `resumen` y `ranking` ignoran los alquileres en curso, respetan el tipo y `top` y no modifican la lista recibida.
4. La validación de `Alquiler` salta tanto al crear como al cambiar el tipo o los minutos; `devuelto` no se puede asignar.
5. `AlquilerAbonado` es un `Alquiler` y `AlquilerAbonado.desde_registro(...)` devuelve un `AlquilerAbonado`.
6. `recaudacion` funciona con cualquier objeto que tenga `importe()`.
7. El informe JSON se escribe con sangría de 2 espacios y las tildes sin escapar.
8. `app.py` nunca se cae por una entrada mal escrita: opción no numérica, tipo inexistente, extra inventado o fecha mal escrita se tratan y se continúa.
9. `tarifas.py` no importa `alquiler.py` e importar los módulos no muestra nada.
10. Los requisitos técnicos del apartado 6.
11. Parte 4: posiciones, claves, mensajes y causas de los errores; los registros correctos se importan aunque haya otros defectuosos; el desempate del ranking.
