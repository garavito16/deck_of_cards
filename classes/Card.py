class Card:

    suits = ("♠","♥","♣","♦")

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} de {self.suit} : {self.point_val} puntos")

    def card_info_short(self):
        return f"{self.string_val} {self.suit}"

    @classmethod
    def get_suits(cls):
        return cls.suits

    def get_point(self):
        return self.point_val