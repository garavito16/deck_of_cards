
from os import system
from classes.WorkCarts import WorkCarts
from classes.Player import Player
system("cls")
print("****** Bienvenidos a MUNDI JUEGOS ******")
print("****************************************")


validator = False

while(validator == False):
    print("***************** MENU *****************")
    print("****************************************")
    print("*** Tenemos disponibles los juegos : ***")
    print("****************************************")
    print("1. Nadie sabe para quien trabaja *******")
    print("2. Carta Mayor *************************")
    print("****************************************")
    option = input("Ingrese el número del juego: ")
    system("cls")
    print("****************************************")
    if(option == "1"):
        print("Usted a eligido 'Nadie sabe para quien trabaja'")
        validator = True
    elif(option == "2"):
        print("Usted a eligido 'Carta Mayor'")
        validator = True
    else:
        print("La opción es incorrecta")
        print("****************************************")


validator = False

while (validator == False):
    print("****************************************")
    cant_players = input("Ingrese la cantidad de jugadores: ")
    if cant_players.isdigit():
        cant_players = int(cant_players)
        validator = True
    else:
        print("****************************************")
        print("Ingrese una cantidad correcta de jugadores")

list_players = []
name = ""
for i in range(cant_players):
    print("****************************************")
    name = input(f"Ingrese el alias del jugador {i+1}: ")
    list_players.append(Player(name))

system("cls")

print("****************************************")
option_cart = ""
num = 1
val_action = False
name_player = ""

if(option == "1"):
    game = WorkCarts(list_players)
    cant_round_player = 0
    while game.initialize_round():
        input(f"Inició la Ronda {num} presionando la tecla enter")
        system("cls")
        for i in range(game.carts_player):
            for i in range(len(list_players)):
                val_action = False
                while val_action == False:
                    name_player = list_players[i].get_alias()
                    cart_select = 0
                    print("****************************************")
                    print("Turno del jugador "+name_player)
                    input("Presiona la tecla enter para jugar tu turno")
                    print("****************************************")
                    #Mostrar cartas del jugador, las cartas de la mesa y la ultima carta de las barajas de los otros jugadores
                    print("Tus cartas son : ")
                    cant_round_player = game.get_deck_assign_carts_player(name_player)
                    print("****************************************")
                    print("Las cartas de la mesa son :")
                    game.get_deck_carts_table()
                    print("****************************************")
                    print("Las últimas cartas de los jugadores son :")
                    game.get_last_cart_players()
                    
                    validator = False
                    while (validator == False):
                        #Pedir que lance una carta
                        print("****************************************")
                        cart_select = input("Ingrese la opción de su carta a jugar : ")
                        if cart_select.isdigit():
                            cart_select = int(cart_select)
                            if cart_select >= 1 and cart_select <= cant_round_player:
                                validator = True
                            else:
                                print("****************************************")
                                print("Usted a ingresado una opción inválida")
                        else:
                            print("Usted a ingresado un valor invalido")

                    system("cls")
                    print("****************************************")
                    print("Usted eligió la carta : "+ game.get_selec_deck_assign_carts_player(name_player,cart_select - 1))
                    print("****************************************")
                    print("Tiene las siguiente opciones : *********")
                    print("****************************************")
                    print("1. LLevar carta de la mesa *************")
                    print("2. Robar baraja de jugador *************")
                    print("3. Solo lanzar carta a la mesa *********")
                    print("****************************************")
                    move = input("¿Que opción elige? ")
                    print("****************************************")
                    if(move == "1"):
                        val_action = game.remove_cart_table(name_player,cart_select - 1)
                        if(val_action == False):
                            print("No existe una carta con el mismo valor que indica")
                            print("Por favor ingrese una acción válida")
                            input("Presiona la tecla para volver a repetir el turno")
                        else:
                            print("Se agregaron las cartas a su baraja")
                            input("Presiona la tecla para continuar con el siguiente turno")
                            val_action = True #Reseteando valor

                    elif(move == "2"):
                        val_action = game.steal_carts_other_player(name_player,cart_select - 1)
                        if(val_action == False):
                            print("No existe baraja que coincida con el valor de tu carta")
                            print("Por favor ingrese una acción válida")
                            input("Presiona la tecla para volver a repetir el turno")
                        else:
                            print("Se agregaron todas las cartas del otro jugador a su baraja")
                            input("Presiona la tecla para continuar con el siguiente turno")
                            val_action = True #Reseteando valor
                        
                    elif(move == "3"):
                        game.add_deck_carts_table(name_player,cart_select - 1)
                        print("Se agrego la carta seleccionada a la mesa")
                        input("Presiona la tecla para continuar con el siguiente turno")
                        val_action = True
                system("cls")
        num += 1
