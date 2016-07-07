A="A"
B="B"
C="C"
D="D"
E="E"
F="F"
G="G"
H="H"
I="I"
win=False
TABLERO=(A+"_| "+B+"  "+C+"\n"+D+"  "+E+"  "+F+"\n"+G+"  "+H+"  "+I)
print(TABLERO)
while win ==False:
	print("turno 1")
	print(TABLERO)
	jugador1=input("ingrese una casilla(A-I): ")
	if jugador1==A and A!="0":
		A="X"
	if jugador1==B and B!="0":
		B="X"
	if jugador1==C and C!="0":
		C="X"
	if jugador1==D and D!="0":
		D="X"
	if jugador1==E and E!="0":
		E="X"
	if jugador1==F and F!="0":
		F="X"	
	if jugador1==G and G!="0":
		F="X"
	if jugador1==H and H!="0":
		H="X"
	if jugador1==I and I!="0":
		I="X"

		jugador2=input("ingrese una casilla(A-I): ")
 

