import math
import random
class player:
    def __init__(self, letter):
       self.letter = letter
    def get_move(self, game):
        pass
class randomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
       pass      
class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
       pass          
