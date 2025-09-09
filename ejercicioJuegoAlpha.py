import random

# Variables globales
nombreUsuario = ""
nombreClase = ""
puntosVida = 0
puntosAtaque = 0
cantidadPociones = 0
vidaEnemigo = 0  # Variable global para la vida del enemigo
puntaje = 0
enemigosDerrotados = 0

#Banderas
jugadorDefensa=0
enemigoDefensa=0
jugadorAtaco=False
enemigoAtaco=False

#Iniciar Juego
def mainGame():
    opcionMenu="0"
    while(opcionMenu!="3"):
        #opcionMenu=input("****Bienvenido a la gruta****\n1.Empezar Partida\n2.Tabla de puntuaciones\n3.Salir \n")
        print("""
 ██████╗ ██████╗ ██╗   ██╗████████╗ █████╗     ██████╗ ██████╗  ██████╗ 
██╔════╝ ██╔══██╗██║   ██║╚══██╔══╝██╔══██╗    ██╔══██╗██╔══██╗██╔════╝ 
██║  ███╗██████╔╝██║   ██║   ██║   ███████║    ██████╔╝██████╔╝██║  ███╗
██║   ██║██╔══██╗██║   ██║   ██║   ██╔══██║    ██╔══██╗██╔═══╝ ██║   ██║
╚██████╔╝██║  ██║╚██████╔╝   ██║   ██║  ██║    ██║  ██║██║     ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝      ╚═════╝ 
                                                                        
""")
        print("""
  _________________________________________________
 |                                                 |
 |        1. Empezar Partida                       |
 |        2. Tabla de puntuaciones                 |
 |        3. Salir                                 |
 |_________________________________________________|
""")


        opcionMenu=input("Opcion: ")
        match opcionMenu:
            case "1":
                startGame()
            case "2":
                score()
            case "3":
                print("Hasta la proxima!")
                break
            case _:
                print("Opcion invalida")

#Iniciar Juego
def startGame():
    while True:
        print("""
  ________________________________
 |                                |
 |        1. Elegir clase         |
 |        2. Regresar             |
 |________________________________|
""")

        opcionMenu = input("Opcion: ")
        match opcionMenu:
            case "1":
                elegirClase()
            case "2":
                return
            case _:
                print("Opcion no valida")

#Tabla de puntuaciones
def score():
    global nombreUsuario, puntaje, puntosAtaque, vidaEnemigo, nombreClase
    
    if nombreUsuario == "":
        print("""
  ________________________________
 |                                |
 |     No hay puntuaciones        |
 |________________________________|
""")
    else:
        print(f"""
  ________________________________
 |        PUNTUACIÓN ACTUAL       |
 |________________________________|
 |  Nombre de usuario: {nombreUsuario:<15}|
 |  Clase:              {nombreClase:<15}|
 |  Puntaje:            {puntaje:<15}|
 |________________________________|
""")

    while True:
        print("""
  ________________________
 |                        |
 |      1. Regresar       |
 |________________________|
""")
        opcionMenu = input("Selecciona una opción: ")
        match opcionMenu:
            case "1":
                return 
            case _:
                print("Opción no válida. Intenta de nuevo.")

#Menú clase
def elegirClase():
    opcionMenu="0"
    while(opcionMenu!="4"):
        print("""
  ________________________________
 |                                |
 |        1. Guerrero 🛡️           |
 |        2. Mago 🔮               |
 |        3. Asesino 🗡️            |
 |        4. Regresar 🔙           |
 |________________________________|
""")


        opcionMenu = input("Selecciona una clase: ")

        match opcionMenu:
            case "1"|"2"|"3":
                generarPj(opcionMenu)
            case "4":
                return
            case _:
                print("Opcion Invalida")

#Creación del jugador
def generarPj(opcionMenu):
    global nombreUsuario, nombreClase, puntosVida, puntosAtaque, cantidadPociones
    nombreUsuario=input("Ingresa tu nombre de usuario: ")
    match opcionMenu:
        case "1":
            nombreClase ="Guerrero"
            puntosVida = 1600
            puntosAtaque = random.randint(500, 700)
            cantidadPociones = 3
        case "2":
            nombreClase ="Mago"
            puntosVida = 1200
            puntosAtaque = random.randint(700, 900)
            cantidadPociones = 6
        case "3":
            nombreClase ="Asesino"
            puntosVida = 1000
            puntosAtaque = random.randint(900, 1200)
            cantidadPociones = 4
    print("""
  ________________________________
 |                                
 |  Nombre de Usuario: {0:<20}  
 |  Clase:            {1:<20}  
 |  Puntos de Vida:   {2:<20}  
 |  Puntos de Ataque: {3:<20}  
 |  Cantidad de Pociones: {4:<20}
 |________________________________
""".format(nombreUsuario, nombreClase, puntosVida, puntosAtaque, cantidadPociones))
      
    seleccionarDificultad()

def seleccionarDificultad():
    opcionMenu="0"
    while(opcionMenu!="4"):
        print("""
  ________________________________
 |                                |
 |        1. Fácil (3 enemigos)   |
 |        2. Normal (6 enemigos)  |
 |        3. Difícil (9 enemigos) |
 |        4. Regresar             |
 |________________________________|
""")

        opcionMenu = input("Selecciona la dificultad: ")

        match opcionMenu:
            case "1"|"2"|"3":
                iniciarPartida(opcionMenu)
            case "4":
                return
            case _:
                print("Opcion no Valida")

def iniciarPartida(dificultad):
    global vidaEnemigo, puntosVida, enemigosDerrotados, puntaje
    match(dificultad):
        case "1":
            cantidadEnemigos=3
        case "2":
            cantidadEnemigos=6
        case "3":
            cantidadEnemigos=9
    for i in range(int(cantidadEnemigos)):
        vidaEnemigo=random.randint(975,1350)
        ataqueEnemigo=random.randint(330,520)
        while(vidaEnemigo>0 and puntosVida>0):
            print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                                       ┃
  ┃     💥  Vida del Jugador:  {0:<5}  💀    ┃
  ┃     🧟  Vida del Enemigo: {1:<5}  ⚔️    ┃
  ┃                                       ┃
  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""".format(puntosVida, vidaEnemigo))

            turnoJugador()
            turnoEnemigo(ataqueEnemigo)
            if(vidaEnemigo<=0):
                print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                                       ┃
  ┃       🎉 ¡HAS DERROTADO AL ENEMIGO!    ┃
  ┃                                       ┃
  ┃       💰 ¡Obtuviste 300 puntos!       ┃
  ┃                                       ┃
  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

                enemigosDerrotados += 1
                puntaje += 300
                break
            if(puntosVida<=0):
                print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                                       ┃
  ┃       💀  GAME OVER  💀               ┃
  ┃                                       ┃
  ┃      ⚔️ Has sido derrotado ⚔️         ┃
  ┃                                       ┃
  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

                break
    print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                                       ┃
  ┃       🎉 ¡HAS DERROTADO A {0} ENEMIGOS! 🎉  ┃
  ┃                                       ┃
  ┃       🎮 Tu puntaje final es: {1}       ┃
  ┃                                       ┃
  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""".format(enemigosDerrotados, puntaje))

    print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                                       ┃
  ┃         🚨 FIN DE LA PARTIDA 🚨         ┃
  ┃                                       ┃
  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
    print("¿Jugar otra partida?")
    return

def turnoJugador():
    global vidaEnemigo, puntosVida, cantidadPociones, puntosAtaque, jugadorDefensa, enemigoAtaco, jugadorAtaco
    
    if(puntosVida>0):
        print("<<-Turno del jugador->>")
        if(puntosVida>jugadorDefensa and enemigoAtaco==False):
            puntosVida-=jugadorDefensa
        jugadorDefensa=0
        
        while True:
            print("1.Atacar\n2.Usar pocion\n3.Defenderse\n")
            opcionMenu=input(">> ")
            match opcionMenu:
                case "1":
                    #dano = random.randint(430, 650)
                    jugadorAtaco=True
                    dano = puntosAtaque+random.randint(-15, 15)
                    vidaEnemigo -= dano
                    print(f"🔵 Has atacado al enemigo y causado {dano} de daño!!")
                    break
                case "2":
                    jugadorAtaco=False
                    if cantidadPociones > 0:
                        cantidadPociones -= 1
                        puntosVida += 400
                        print("🔵 Has usado una poción y recuperado 400 puntos de vida!!")
                        break
                    else:
                        print("No tienes pociones!")
                case "3":
                    jugadorAtaco=False
                    jugadorDefensa = random.randint(100, 200)
                    puntosVida += jugadorDefensa
                    print(f"🔵 Has levantado tu defensa contra el proximo ataque por {jugadorDefensa} puntos!!")
                    break
                case _:
                    print("Opción no válida")

def turnoEnemigo(ataqueEnemigo):
    global puntosVida, vidaEnemigo, enemigoDefensa, jugadorAtaco, enemigoAtaco
    
    if(vidaEnemigo>0):
        print("<<-Turno del enemigo->>")  
        if(vidaEnemigo>enemigoDefensa and jugadorAtaco==False):
            vidaEnemigo-=enemigoDefensa
        enemigoDefensa=0

        opcionMenu=random.randint(1,2)
        match str(opcionMenu):
            case "1":
                enemigoAtaco=True
                puntosVida -= ataqueEnemigo
                print("🔴 El enemigo ha atacado y causado ", ataqueEnemigo, "puntos de daño!!")
            case "2":
                enemigoAtaco=False
                enemigoDefensa = random.randint(100, 200)
                vidaEnemigo += enemigoDefensa
                print(f"🔴 El enemigo levanta su defensa contra el proximo ataque en {enemigoDefensa} puntos!!")
            case _:
                print("Opción no válida")

mainGame()
