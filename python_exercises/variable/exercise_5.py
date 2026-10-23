text = "Desarrollo Web en Entorno Servidor"

print(len(text))
# El texto tiene 34 caracteres y podemos verlo con el len()
print("web" in text.upper())
# "web" no está dentro del texto porque lo comprueba si está tal cual así, y como en el texto está en mayusculas, da False
print("web" in text.lower())
# Ahora "web" si está porque estamos haciendo la comprobación convirtiéndolo a minúsculas
