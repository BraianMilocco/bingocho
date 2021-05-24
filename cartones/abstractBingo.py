
class AbstractBingo():
    def __init__(self, bingo_generator, *args):
        self.numbers = [ bingo_generator.get_number( arg ) for arg in args ]         

    def get_numbers(self):
        return numbers

    def get_card(self):
        print("Abstract Method")
        raise NotImplementedError()