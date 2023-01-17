texto = "Esto es un texto para el ejemplo que vamos a realizar"
#empieza y termina con
print("La cadena empieza con ",texto.startswith("Esto"))
print("La cadena termina con ",texto.lower().endswith("Realizar".lower()))

#alinear
#centrado
print(texto.center(80, "/"))
longitudCadena = len(texto)
print(longitudCadena)
print(texto.center(longitudCadena+7, "-"))
#izquierda
print(texto.ljust(80, "-"))
#derecha
print(texto.rjust(80, "0"))

#eliminar espacios en blanco
texto = "     Esto es una cadena con espacios en blanco y algunos caracteres raros */4876-.mb?\\\+    "
print(texto)
print("Cadena sin espacios en blanco: ")
print(texto.strip())


#sustituit caracter
print(texto.replace("-", "hola"))
textoModificado = texto.replace("-", "hola")
print(textoModificado)
print(texto)