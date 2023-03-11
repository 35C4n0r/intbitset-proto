class BitSet:
    def __init__(self):
        self.bitset = 0
    
    def add_element(self, integer):
        self.bitset |= 1 << integer

        

