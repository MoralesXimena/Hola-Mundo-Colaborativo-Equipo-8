Algoritmo sin_titulo
		Definir tablero[3,3], fila, col Como Entero
		Definir turno, simbolo Como Caracter
		Definir jugador1, jugador2, ganador Como Cadena
		Definir movimientos Como Entero
		Definir archivo Como Texto
		
		Escribir "Ingrese el nombre del Jugador 1 (X):"
		Leer jugador1
		Escribir "Ingrese el nombre del Jugador 2 (O):"
		Leer jugador2
		
		Para fila <- 0 Hasta 2
			Para col <- 0 Hasta 2
				tablero[fila, col] <- " "
			FinPara
		FinPara
		
		movimientos <- 0
		turno <- "X"
		ganador <- ""
		
		Mientras ganador = "" Y movimientos < 9
			MostrarTablero(tablero)
			
			Si turno = "X" Entonces
				Escribir jugador1, " (X), elija su posición:"
			Sino
				Escribir jugador2, " (O), elija su posición:"
			FinSi
			
			Repetir
				Escribir "Fila (0-2):"
				Leer fila
				Escribir "Columna (0-2):"
				Leer col
			Hasta Que fila >= 0 Y fila <= 2 Y col >= 0 Y col <= 2 Y tablero[fila, col] = " "
			
			tablero[fila, col] <- turno
			movimientos <- movimientos + 1
			
			Si VerificarGanador(tablero, turno) Entonces
				Si turno = "X" Entonces
					ganador <- jugador1
				Sino
					ganador <- jugador2
				FinSi
				MostrarTablero(tablero)
				Escribir "¡Ganó ", ganador, "!"
			Sino
				Si turno = "X" Entonces
					turno <- "O"
				Sino
					turno <- "X"
				FinSi
			FinSi
		FinMientras
		
		Si ganador = "" Entonces
			MostrarTablero(tablero)
			Escribir "¡Empate!"
			ganador <- "Empate"
		FinSi
		
		Abrir archivo <- "historial.txt" Para Agregar
			Escribir archivo, "Ganador: ", ganador
			Cerrar archivo
			
FinAlgoritmo

Funcion VerificarGanador(tablero[3,3], simbolo) : Logico
		Definir i Como Entero
		
		Para i <- 0 Hasta 2
			Si tablero[i,0] = simbolo Y tablero[i,1] = simbolo Y tablero[i,2] = simbolo Entonces
				VerificarGanador <- Verdadero
				Salir
			FinSi
		FinPara
		
		Para i <- 0 Hasta 2
			Si tablero[0,i] = simbolo Y tablero[1,i] = simbolo Y tablero[2,i] = simbolo Entonces
				VerificarGanador <- Verdadero
				Salir
			FinSi
		FinPara
		
		Si tablero[0,0] = simbolo Y tablero[1,1] = simbolo Y tablero[2,2] = simbolo Entonces
			VerificarGanador <- Verdadero
			SinoSi tablero[0,2] = simbolo Y tablero[1,1] = simbolo Y tablero[2,0] = simbolo Entonces
			VerificarGanador <- Verdadero
		Sino
			VerificarGanador <- Falso
		FinSi
FinFuncion


SubProceso MostrarTablero(tablero[3,3])
	Definir i, j Como Entero
	Escribir "  0 1 2"
	Para i <- 0 Hasta 2
		Escribir Sin Saltar i, " "
		Para j <- 0 Hasta 2
			Escribir Sin Saltar tablero[i,j]
			Si j < 2 Entonces
				Escribir Sin Saltar "|"
			FinSi
		FinPara
		Escribir ""
		Si i < 2 Entonces
			Escribir "  -----"
		FinSi
	FinPara
	
FinAlgoritmo
