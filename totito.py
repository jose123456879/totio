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
TABLERO=(A+"_| "+B+"_|_"+C+"\n"+D+"_| "+E+"_|_"+F+"\n"+G+" | "+H+" | "+I)
print(TABLERO)
while win ==False:
	print("turno 1")
	print(TABLERO)
	jugador1=input("ingrese una casilla(A-I): ")
	if jugador1==A and A!="0":
		A="X"
	if jugador1==B and B!="o":
		B="X"
	if jugador1==C and C!="o":
		C="X"
	if jugador1==D and D!="o":
		D="X"
	if jugador1==E and E!="o":
		E="X"
	if jugador1==F and F!="o":
		F="X"	
	if jugador1==G and G!="o":
		F="X"
	if jugador1==H and H!="o":
		H="X"
	if jugador1==I and I!="o":
		I="X"

	print(TABLERO)
	jugador2=input("ingrese una casilla(A-I): ")

	if jugador2==A and A!="X"
		A="o"		
	if jugador2==B and B!="X"
		B="o"
	if jugador2==C and C!="X"
		C="o"	
	if jugador2==D and D!="X"
		D="o"						
	if jugador2==E and E!="X"
		E="o"			
	if jugador2==F and F!="X"
		F="o"		
	if jugador2==G and G!="X"
		G="o"	
	if jugador2==H and H!="X"
		H="o"
	if jugador2==I and I!="X"
		I="o"			
	print(TABLERO)	