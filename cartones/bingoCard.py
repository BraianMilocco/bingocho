
class BingoCard():
    def __init__(self, number_generator, card_type):
        self.numbers = self.generate_numbers(number_generator,card_type)         

    def get_numbers(self):
        return self.numbers

    def get_card(self):
        numbers = self.get_numbers()
        return {
            "first_line": numbers[0:9],
            "second_line": numbers[9:18],
            "third_line": numbers[18:27],
        }
    
    def generate_numbers(self, number_generator, card_type):
        numbers = []
        for column_number in card_type.get_pattern():
            numbers.append(number_generator.get_number( column_number ))
        
        return numbers