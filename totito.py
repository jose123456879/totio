tablero=[["a", "b", "c"],["d", "e", "f"], ["g", "h", "i"]]
print("bienvenidos a totito")
while win ==False:
	tiro=input("turno de jugador 1")
	tiro_valor=ord(tiro)-65
	tiro_fila=tiro_valor%3
	tiro_columna=tiro_valor//3
	
