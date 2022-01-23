from abc import ABC,abstractmethod
from typing import List
from classes.Player import Player
from classes.Deck import Deck

class Game(ABC):

    def __init__( self, players:List[Player],max_players:int,min_players:int,carts_table:int,carts_player:int,show_carts_table:bool):
        self.players = players
        self.cant_players = len(self.players)
        self.amount_deck = self.get_amount_deck(self.cant_players) #cantidad de barajas
        self.deck = Deck(self.amount_deck)
        self.max_players = max_players              #Maxima cantidad de jugadores para el juego
        self.min_players = min_players              #Minima cantidad de jugadores para el juego
        self.carts_table = carts_table              #Cantidad de cartas para dejar en mesa en cada ronda
        self.carts_player = carts_player            #Cantidad de cartas asignadas para cada jugador durante cada ronda
        self.show_carts_table = show_carts_table    #Flag que decide si los jugadores pueden ver o no las cartas que estan en mesa
        self.deck_carts_player = {}                 #Barajas ganadas por los jugadores
        self.deck_assign_carts_player = {}          #Barajas asignadas por cada ronda a los jugadores (cartas con las que jugaran)
        self.start_deck_carts_player()              #inicializar barajas de los jugadores
        self.deck_carts_table = []                  #cartas en la mesa                
        self.get_deck_carts()

    @staticmethod
    def get_amount_deck(num):
        return int(num/2)

    def get_deck_carts(self):
        return self.deck.show_cards()

    # sumar carta a la mesa de la baraja de un jugador
    def add_deck_carts_table(self,name_player,num):
        cart = self.deck_assign_carts_player[name_player].pop(num) #se quita de la baraja del jugador
        self.deck_carts_table.append(cart)  #se agrega a la mesa
        print("Se sumo la carta a la mesa")

    #ver cartas ganadas hasta ahora por el jugador
    def get_deck_carts_player(self,name_player):
        for i in range(len(self.deck_carts_player[name_player])):
            print(self.deck_carts_player[name_player][i].card_info_short())

    #ver cartas que tiene el jugador en mano para la ronda
    def get_deck_assign_carts_player(self,name):
        num = len(self.deck_assign_carts_player[name])
        for i in range (num):
            print(str(i+1)+" : "+self.deck_assign_carts_player[name][i].card_info_short())
        return num

    #ver carta que seleccionó jugador de sus cartas que tiene en mano
    def get_selec_deck_assign_carts_player(self,name,num):
        return self.deck_assign_carts_player[name][num].card_info_short()

    #valor de la carta que seleccionó jugador de sus cartas que tiene en mano
    def get_selec_value_deck_assign_carts_player(self,name,num):
        return self.deck_assign_carts_player[name][num].get_point()

    #ver cartas en la mesa
    def get_deck_carts_table(self):
        num = len(self.deck_carts_table)
        for i in range(num):
            print(self.deck_carts_table[i].card_info_short())
        return num

    #asignar cartas a la mesa
    def cards_the_table(self):
        num = self.carts_table
        print("Las cartas que se agregaron a la mesa son:")
        while(num > 0):
            cart = self.deck.remove_cart()
            self.deck_carts_table.append(cart)
            if self.show_carts_table:
                print(cart.card_info_short())
            num -= 1

    #inicializar barajas de los jugadores (tanto para acumular cartas ganadas como las que usaran en cada ronda)
    def start_deck_carts_player(self):
        aux = None
        for i in range (self.cant_players):
            aux = self.players[i].alias
            self.deck_carts_player[aux] = []

        if self.carts_player > 0:
            for i in range (self.cant_players):
                aux = self.players[i].alias
                self.deck_assign_carts_player[aux] = []

    #assignar cartas en las rondas
    def assign_cards_round(self):
        num = self.carts_player 
        while(num > 0):
            for i in range (self.cant_players):
                cart = self.deck.remove_cart()
                self.deck_assign_carts_player[self.players[i].alias].append(cart)
            num -= 1
        print("Se asignaron cartas a los jugadores!!!")
        print("****************************************")

    @abstractmethod
    def initialize_round(self):
        raise NotImplementedError("implement method")
        
    #verificar si hay suficientes cartas para otra ronda
    @abstractmethod
    def verify_carts_round(self):
        raise NotImplementedError("implement method")

    # definir el ganador del juego
    def define_player_winner(self):
        points = 0
        player_winner = ""
        for player in self.deck_carts_player:
            print("cantidad de cartas de "+player+" : "+str(len(self.deck_carts_player[player])))
            if(len(self.deck_carts_player[player]) > points):
                points = len(self.deck_carts_player[player])
                player_winner = player
        print("El ganador del juego es "+player_winner+" con "+str(points)+" cartas")