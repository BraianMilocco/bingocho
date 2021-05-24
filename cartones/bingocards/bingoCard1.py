from ..abstractBingo import AbstractBingo
from ..bingoGenerator import BingoGenerator

class BingoType1(AbstractBingo):
    def __init__(self):
        AbstractBingo.__init__( self, bingo_generator,
                                1,1,2,2,3,
                                4,4,5,6,6,
                                7,7,8,8,9
                            )

    def get_card(self):
        numbers = self.get_numbers()
        return {
            "first_line": [
            numbers[0],numbers[2],0,numbers[5],numbers[8],numbers[10],0,0
            ],
            "second_line": [
            0,numbers[3],numbers[4],0,numbers[7],0,numbers[11],numbers[12],0
            ],
            "third_line": [
            numbers[1],0,0,numbers[6],0,numbers[9],0,numbers[13],numbers[14]
            ]
        }