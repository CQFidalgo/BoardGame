#Author: CQFidalgo

# -*- encoding: utf-8 -*-

import random
import math
import string

#Ancho tiene que ser mayor o igual que alto
ancho=10
alto=10
golpes=0
coord=[] #Crea una lista en la que se iran almacenando las coordenadas

def main(): #Se encarga de recoger por teclado el nivel y de iniciar el juego,llamando a "nivel", la variable "nivel" es la unica que usa, es local.
    
    print "Introduzca el nivel que desea jugar :  " #Le pide por pantalla al usuario que introduzca el nivel deseado.
    nivel = raw_input() #Recoge por teclado el nivel que ha elegido el usuario y lo almacena en la variable "nivel".
    if(nivel.isdigit()==False): #Valida el dato, si no es un digito da error.
        print " El valor introducido no es valido." #Imprimimos un mensaje de error por pantalla informando del error.
        main() #Vuelve a llamar al procedimiento para que vuelva a pedir el nivel hasta que se introduzca bien.
    elif nivel<"1": #Valida el dato, si el nivel es menor de 0 da error.
        print " El valor introducido no es valido." #Imprimimos un mensaje de error por pantalla informando del error.
        main() #Vuelve a llamar al procedimiento para que vuelva a pedir el nivel hasta que se introduzca bien.
    else: #Valida el dato, si llega hasta este punto es que es correcto y empezara el juego.
        tablero(nivel) #Llama a la funcion "tablero" pasandole el parametro "nivel".

def actualizar (matriz,fil,col): #Se encarga de hacer el golpe en el tablero, para ello se actua diferente segun donde se de el golpe, si se hace en los bordes del tablero o en el centro. Recibe como argumentos: matriz, fil y col, con ellos hara el golpe y devuelve la matriz ya actualizada
    
    # print str(fil) + " " + str(col) #imprime los aleatorios generados.

    matriz[fil][col]=cambio(matriz[fil][col])  #Cambio en las casillas centrales.
    #Cambios en los bordes del tablero.
    if col!=0: #Si la columna es diferente de 0.
        matriz[fil][col-1]=cambio(matriz[fil][col-1])
        if col!=1: #Si la columna es diferente de 0 y 1.
            matriz[fil][col-2]=cambio(matriz[fil][col-2])

    if fil!=0: #Si la fila es diferente de 0.
        matriz[fil-1][col]=cambio(matriz[fil-1][col])
        if col!=ancho-1: #Si la fila es diferente de 0 y la columna de 9.
            matriz[fil-1][col+1]=cambio(matriz[fil-1][col+1])
            if col!=ancho-2: #Si la fila es diferente de 0 y la columna de 8 y 9.
                matriz[fil-1][col+2]=cambio(matriz[fil-1][col+2])
        if col!=0: #Si la fila y la columna son diferentes de 0.
            matriz[fil-1][col-1]=cambio(matriz[fil-1][col-1])
            if col!=1: #Si la fila es diferente de 0 y la columna de 0 y 1.
                matriz[fil-1][col-2]=cambio(matriz[fil-1][col-2])
        if fil!=1: #Si la fila es diferente de 0 y 1.
            matriz[fil-2][col]=cambio(matriz[fil-2][col])
            if col!=ancho-1:#Si la fila es diferente de 0 y 1 y la columna de 9.
                matriz[fil-2][col+1]=cambio(matriz[fil-2][col+1])
            if col!=0: #Si la fila es diferente de 0 y 1 y la columna de 0.
                matriz[fil-2][col-1]=cambio(matriz[fil-2][col-1])

    if col!=ancho-1: #Si la columna es diferente de 9
        matriz[fil][col+1]=cambio(matriz[fil][col+1])
        if col!=ancho-2: #Si la columna es diferente de 8 y 9.
            matriz[fil][col+2]=cambio(matriz[fil][col+2])


    if fil!=alto-1: #Si la fila es diferente de 9.
        matriz[fil+1][col]=cambio(matriz[fil+1][col])
        if col!=ancho-1: #Si la fila y la columna son diferentes de  9.
            matriz[fil+1][col+1]=cambio(matriz[fil+1][col+1])
            if col!=ancho-2: #Si la fila es diferente de 9 y la columna de 8 y de 9.
                matriz[fil+1][col+2]=cambio(matriz[fil+1][col+2])
        if col!=0: #Si la fila es diferente de 9 y la columna de 0.
            matriz[fil+1][col-1]=cambio(matriz[fil+1][col-1])
            if col!=1: #Si la fila es diferente de 9 y la columna de 0 y 1.
                matriz[fil+1][col-2]=cambio(matriz[fil+1][col-2])
        if fil!=alto-2: #Si la fila es diferente de 8 y 9.
            matriz[fil+2][col]=cambio(matriz[fil+2][col])
            if col!=ancho-1: #Si la fila es diferente de 8 y 9 y la columna de 9
                matriz[fil+2][col+1]=cambio(matriz[fil+2][col+1])
            if col!=0: #Si la fila es diferente de 8 y 9 y la columna de 0.
                matriz[fil+2][col-1]=cambio(matriz[fil+2][col-1])
    
    return matriz  #Retorna la matriz ya actualizada con las coordenadas que acabamos de jugar.

def juego (matriz,nivel): # Se encarga de pedir las coordenadas al usuario y hacer la validacion de la entrada por teclado ademas de jugar hasta que el tablero este lleno de puntos. Esto lo hace mediante un bucle en el cual hasta que el metodo comprobar no detecta que se ha llenado de ceros el tablero se piden coordenadas y se golpean en el tablero. Recibe como argumentos matriz y nivel, ademas de usar la variable golpes y la lista coord.Crea las variables locales i1, i2 y v, las dos primeras son las coordenadas que introduce el usuario por teclado y "v" es lo que introduce el usuario por teclado al decidir si quiere seguir jugando.
    golpes=0 #Se inicia la variable a 0.
    while comprobar(matriz) == True: #El bucle es el juego, pedira coordendas hasta que el tablero este lleno de puntos.
        print "Introduzca las coordenadas (Letra Numero) : "
	i = raw_input() #Almacena en la variable "i" lo que el usuario introduce por teclado.
	if i=="salir": #En el momento en el que el usuario introduzca la palabra salir se llamara a la funcion predefinida "quit()".
	    quit()
	elif i=="deshacer": #Si el usuario escribe en teclado "deshacer" vuelve a la situacion anterior dando otra vez el mismo golpe. 
	    if len(coord)==0: #Si la longitud de la lista coord es 0, significa que no hay ninguna coordenada almacenada
		print"No hay jugadas previas" #y que lo se puede deshacer ninguna jugada
	    else: #Si hay alguna coordenada almacenada...
	        i = coord.pop() #Elimina el ultimo golpe y lo almacenamos en la variable i.
	        matriz=actualizar(matriz,i[0],i[1]) #Actualiza la matriz con las coordenadas almacenadas en la variable "i".
	        imprimir(matriz,golpes) #Imprime la matriz  
        else:
	    if len(i)==0: #Comprueba si el usuario ha introducido algo por teclado, si no es asi, muestra un mensaje de error,
		print "No ha introducido ninguna coordenada" #y vuelve a pedir las coordenadas.
	    else:
	        if i[0].isalpha()==True: #Si el primer elemento que introduce el usuario es una letra lo almacena en la variable "i1".
                    i1=i[0]
                    if i1.islower(): #Si es minuscula calcula la diferencia en el codigo ASCII entre esa letra y la primera minuscula del 
                        i1=ord(i1)-ord('a') #alfabeto y esa diferencia sera el valor numerico.
                    elif i1.isupper(): #Si es mayuscula calcula la diferencia en el codigo ASCII entre esa letra y la primera mayuscula del 
                        i1=ord(i1)-ord('A') #alfabeto y esa diferencia sera el valor numerico.

                    if i1>=0 and i1<=alto-1 : #Si la representacion numerica del primer elemento esta en el rango comprueba el segundo elemento.
		        if i[1:].isdigit()==True: #Si el elemento de la posicion 1 en adelante es un numero se almacena en la variable "i2".
			    i2=int(i[1:])
			    if i2>=0 and i2<=ancho-1: #Si la variable i2 esta en el rango se procede a dar el golpe en el tablero.
				golpes+=1 #Aumenta el contador de golpes en 1.
			    	matriz=actualizar(matriz,i1,i2) #Actualiza la matriz dando el golpe en las coordenadas que introdujo el usuario.
			    	imprimir(matriz,golpes) #Imprime la matriz por pantalla.
			    	coord.append((i1,i2)) #Anade a la lista coord las coordenadas que acabamos de golpear.
			    	
			    else:
				print"Las coordenadas introducidas son incorrectas, intentelo otra vez" #Imprime un mensaje de error por pantalla.
			    
		        elif i[1].isalpha():  #Comprueba si el elemento de la posicion 1 en adelante son letras
			    print"Las coordenadas introducidas son incorrectas,intentelo otra vez" #Imprime un mensaje de error por pantalla.	
		        elif i[2:].isdigit()==True: #Esta opcion es por si el formato en vez de por meter letra y numero seguidos, hay un espacio
			    i2=int(i[2:]) #por medio, si el elemento de la posicion 2 en adelante es un numero se almacena en la variable i2.
			    if i2>=0 and i2<=ancho-1: #Si i2 esta en el rango se procede a dar el golpe en el tablero.
				golpes+=1#Aumenta el contador de golpes en 1.
			        matriz=actualizar(matriz,i1,i2) #Actualiza la matriz dando el golpe en las coordenadas que intrudujo el usuario.
			        imprimir(matriz,golpes) #Imprime la matriz por pantalla.
			        coord.append((i1,i2)) #Anade a la lista coord las coordenadas que acabamos de golpear.
			        
			    else:
			       print"Las coordenadas introducidas son incorrectas, intentelo otra vez" #Imprime un mensaje de error por pantalla.
		        else:
		            print"Las coordenadas introducidas son incorrectas, intentelo otra vez" #Imprime un mensaje de error por pantalla.
                    else:
                        print"Las coordenadas introducidas son incorrectas, intentelo otra vez" #Imprime un mensaje de error por pantalla.
                else:
                    print"Las coordenadas introducidas son incorrectas, intentelo otra vez" #Imprime un mensaje de error por pantalla.
    
    puntuaciones(golpes,nivel) #Llama al procedimiento "puntuaciones" para actualizar el fichero de puntuaciones.					
    print #Imprime un salto de linea
    print "El juego ha terminado"
    print "Pulse 1 si desea volver a jugar" #Se le ofrece al usuario seguir jugando.
    v=raw_input() #Almacena en la variable "v" lo que el usuario introduce por teclado.
    if v=="1": #Si es un uno volvera a iniciarse el juego, si introduce otro valor, saldra de el
        main()
    print	

def tablero (nivel): #Crea el tablero y lo "llena" de golpes aleatoriamente basandose en el nivel que ha introducido el usuario, recibe como parametro la variable nivel. Y crea las variables locales cont, i y j, el contador lo usa para generar tantos golpes como nivel haya introducido el usuario, i y j es la coordenada que se crea.
    matriz = [[0 for x in range (int(alto))]for x in range (int(ancho))] #Crea la matriz con el rango deseado.
    cont=0 #Inicia el contador a 0.
    while (cont<int(nivel)): #Bucle que creara tantos golpes como nivel haya introducido el usuario.
        
        i=random.randint(0,ancho-1) #Se obtiene aleatoriamente una coordenada para las filas.
        j=random.randint(0,alto-1) #Se obtiene aleatoriamente una coordenada para las columnas.
        matriz = actualizar(matriz,i,j) #Se da el golpe aleatorio en la matriz
        cont+=1 #Aumenta el contador, el bucle parara cuando haya dado tantos golpes como niveles haya introducido el usuario.

    imprimir(matriz,golpes) #Imprime la matriz.
    juego(matriz,nivel) #Llama a la funcion que se encarga de "jugar".
    
def cambio (c): #Cambia el valor de los elementos del tablero, recibe como argumento la variable "c", que es el elemento del tablero a modificar.
    #Retorna el elemento ya cambiado.
    if c==0: #Si en la coordenada de "la mancha" habia un elemento 0, este pasa a 1.
        c=1
    elif c==1: #Si en la coordenada de "la mancha habia un elemento 1 , este pasa a 0.
        c=0
    return c #Retorna el elemento ya cambiado.
    
def imprimir (matriz,golpes): #Imprime por pantalla el tablero y los golpes que se van dando en el. Recibe como argumentos la matriz y la variable golpes.
    x=0 
    p=65 #La A mayuscula es el caracter 65 del codigo ASCII,
    print chr(27)+"[4m"+"  |",
    
    while x<=ancho-1:
        print "  "+str(x),
        x+=1
    print chr(27)+"[0;0m"+"    "+chr(27)+"[0;0m",
    for j in matriz: #Recorre las filas imprimiendo lo siguiente
        print '' 
        print chr(p)+' |  ', #Imprime las letras en mayuscula seguidas de una barra a la izquierda del tablero
        for k in j: #Para cada elemento de la matriz...
            if k == 0: #Cambia los ceros por puntos.
                print ".",
            elif k == 1: #Cambia los unos por equis.
                print "x",

            print ' ',
        p+=1 #Cada linea es una letra, cada vez que se hace el bucle hasta que este acaba, se pone una letra del alfabeto en la columna izquierda.
    print''	
    print
    print "Puntos: ", golpes #Imprime debajo del tablero los puntos que lleva dados en el juego actual.
    print

def comprobar(matriz): #Comprueba si la matriz esta llena de ceros, en el momento en el que hay tantos ceros como elementos de la matriz, retorna el valor "False", para ello recorre con un bucle la matriz y cuenta los ceros con un contador, comparandolos con el total de elementos de la matriz. Recibe como argumento la matriz. Crea la variable local cont, que es el contador que almacena el numero de ceros que encuentra en la matriz. Devuelve como argumento False o True, segun el numero de ceros que haya encontrado.
    cont=0 #Inicia el contador a 0.
    for j in matriz:      
        for k in j:  #Recorre la matriz.
            if k==0:  #Localiza los ceros en la matriz.
                cont+=1 #Cada vez que encuentra un 0 aumentamos el contador.
    if cont==ancho*alto: #En el momento en el que haya tantos ceros como elementos en la matriz retorna el valor "False"  
        return False
    else: #Mientras haya algun elemento diferente a cero, la funcion devuelve el valor "False"
        return True
			
def puntuaciones(golpes,nivel): #Crea el fichero de puntuaciones y guarda en el las puntuaciones con su respectivo nivel, las guarda en un formato especial para que no haya problemas en jugar niveles de hasta 6 digitos y lo ordena. Recibe como argumento las variables golpes y nivel, que luego guardara en el fichero. Crea las variables locales f, linea, numlineas, encontrado, nivelFichero, golpesFichero y lista_puntuaciones.
    try: #Intentamos abrir el archivo, si existe buscamos el nivel que hemos jugado en el.
    	f=open("FicheroPuntuaciones.txt","r+") #Se abre el fichero en modo lectura/escritura.
    	linea=f.readline() #Lee la primera linea del fichero y la almacena en la variable "linea".
        numlineas=0 #Inicializa la variable numlineas a 0.
        encontrado = False #Inicializa la variable "encontrado" en valor falso, si el nivel que se ha jugado ya existe, pasara a verdadero.
        while linea != "" : #Se crea una lista con lo que hay en cada linea del fichero.
	    numlineas+=1 #Cada vez que se hace el bucle, el contador "numlineas" suma uno.
	    nivelFichero = linea.split()[0] #Almacena en la variable "nivelFichero" lo que hay hasta el primer espacio del fichero.
	    golpesFichero = linea.split()[1] #Almacena en la variable "golpesFichero" lo que hay despues del primer espacio del fichero.
    	    if str(nivel) == nivelFichero: #Comprueba si el nivel que se ha jugado ya existe en el fichero.
		encontrado = True #En el momento en el que se entra en el "if" el estado de la variable encontrado pasa a verdadero.
		if golpes < int(golpesFichero): #Comprueba si el usuario ha batido el anterior record de ese nivel.
		    f.seek(0) #Pone el puntero al principio del archivo.
		    for i in range (numlineas-1): #Posiciona el puntero en la linea anterior a la del nivel que va a cambiar.
		        f.readline() #Hace un salto de linea desde la anterior y se posiciona al principio de la linea que se va a cambiar.
		    f.write(format(int(nivel),"5d")+" "+format(golpes, "5d")+"\n") #Escribe el nivel y la puntuacion en el fichero. 
		    print "Enhorabuena, ha superado el record del nivel ", nivel #Escribe por pantalla un mensaje de felicitacion al usuario.
		else: #Si ha hecho mas golpes de los almacenados en el fichero no escribe nada en este.
		    print "No has mejorado el record anterior" #Informa por pantalla al usuario de que no ha mejorado el record.
	    linea=f.readline() 
        if not encontrado: #Si la variable encontrado no ha cambiado de estado entonces escribimos al final del fichero.
	    f.write(format(int(nivel),"5d")+" "+format(golpes, "5d")+"\n") #Escribe el nivel y la puntuacion en el fichero.
	    print "Ha jugado el nivel ",nivel," por primera vez" #Informa por pantalla al usuario de que ha jugado el nivel por primera vez.
        f.seek(0) #Pone el puntero al principio del archivo
        lista_puntuaciones=sorted(file("FicheroPuntuaciones.txt")) #Abre el fichero, lo recorre, lo ordena y lo almacena en la lista
        file("FicheroPuntuaciones.txt","w").writelines(lista_puntuaciones) #Escribe la lista ordenada en el fichero
        f.close() #Cierra el fichero.

    except IOError: #Si el fichero no existe se crea y se escribe en el primer nivel jugado.
        f = open ("FicheroPuntuaciones.txt","w") #Crea y abre en modo escritura el fichero.
        f.write (format(int(nivel),"5d")+" "+format(golpes,"5d")+"\n") #Escribe el primer nivel que jugamos con su puntuacion en el fichero.
        f.close() #Cierra el fichero.

    

    
main()
