
class BingoTypeAbstract():
    def __init__(self,pattern):
        self.pattern = pattern

    def get_pattern(self):
        return self.pattern

class BingoType1(BingoTypeAbstract):
    def __init__(self):
        pattern = [
            1,2,0,4,0,6,7,0,0,
            0,2,3,0,5,0,7,8,0,
            1,0,0,4,0,6,0,8,9
        ]
        BingoTypeAbstract.__init__(self, pattern)

class BingoType2(BingoTypeAbstract):
    def __init__(self):
        pattern = [
                1,0,3,4,0,6,0,8,0,
                0,2,3,0,5,0,7,0,9,
                1,0,0,4,0,6,0,8,9
            ]
        BingoTypeAbstract.__init__(self, pattern)


class BingoType3(BingoTypeAbstract):
    def __init__(self):
        pattern = [
            0,2,0,4,5,0,7,8,0,
            1,0,3,4,0,6,0,0,9,
            0,2,3,0,5,0,7,0,9
        ]
        BingoTypeAbstract.__init__(self, pattern)    

class BingoType4(BingoTypeAbstract):
    def __init__(self):
        pattern = [
            1,0,3,0,5,0,7,8,0,
            1,0,0,4,0,6,7,0,9,
            0,2,3,0,5,0,0,8,9
        ]
        BingoTypeAbstract.__init__(self, pattern) 


class BingoType5(BingoTypeAbstract):
    def __init__(self):
        pattern = [
            0,2,0,0,5,6,7,0,9,
            0,2,3,0,5,0,7,8,0,
            1,0,3,4,0,6,0,0,9
        ]
        BingoTypeAbstract.__init__(self, pattern) 


class BingoType6(BingoTypeAbstract):
    def __init__(self):
        pattern = [
            1,0,3,0,5,6,0,0,9,
            0,2,0,4,5,0,7,8,0,
            0,2,0,4,0,6,0,8,9
        ]
        BingoTypeAbstract.__init__(self, pattern)
 