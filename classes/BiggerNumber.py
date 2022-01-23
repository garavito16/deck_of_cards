
from typing import List
from classes.Game import Game
from classes.Player import Player

class BiggerNumber(Game):

    def __init__(self, players: List[Player]):
        super().__init__(players,2,2,2,0,False)

    def initialize_round(self):
        print("corriendo juegoo!!!")
        # return super().play()