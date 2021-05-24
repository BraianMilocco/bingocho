from bingoCard import BingoCard
from bingoGenerator import BingoGenerator
from bingoType import BingoType1, BingoType2, BingoType3
from bingoType import BingoType4, BingoType5, BingoType6

if __name__ == "__main__":

    
    bingo_generator = BingoGenerator()
    card =BingoCard(bingo_generator,BingoType1() )
    print(card.get_card())
    card =BingoCard(bingo_generator,BingoType2() )
    print(card.get_card())
    card =BingoCard(bingo_generator,BingoType3() )
    print(card.get_card())
    card =BingoCard(bingo_generator,BingoType4() )
    print(card.get_card())
    card =BingoCard(bingo_generator,BingoType5() )    
    print(card.get_card())
    card =BingoCard(bingo_generator,BingoType6() )        
    print(card.get_card())
        
