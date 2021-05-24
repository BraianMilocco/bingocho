import random

class BingoGenerator():
    def __init__(self):
        self.column_1 = [ n for n in range(1,10)]
        self.column_2 = [ n for n in range(10,20)]
        self.column_3 = [ n for n in range(20,30)]
        self.column_4 = [ n for n in range(30,40)]
        self.column_5 = [ n for n in range(40,50)]
        self.column_6 = [ n for n in range(50,60)]
        self.column_7 = [ n for n in range(60,70)]
        self.column_8 = [ n for n in range(70,80)]
        self.column_9 = [ n for n in range(80,91)]

    def get_random(self, list_):
        position = random.randint(0, (len(list_)-1))

        number = list_[position]
        list_.remove(number)

        return number

    def get_number(self,column_position):
        if column_position == 0:
            return 0 
        list_ = self.get_list()
        
        return self.get_random(list_[str(column_position)])


    def get_list(self):
        return {
        "1": self.column_1,
        "2": self.column_2, 
        "3": self.column_3, 
        "4": self.column_4, 
        "5": self.column_5, 
        "6": self.column_6, 
        "7": self.column_7, 
        "8": self.column_8, 
        "9": self.column_9 
        }        
