from bitset import BitSet


class intbitset:
    def __init__(self, rhs=0, preallocate=-1, trailing_bits=0) -> None:
        self.rhs=rhs
        self.preallocate=preallocate
        self.trailing_bits=trailing_bits
        self.sanity_checks="CFG_INTBITSET_ENABLE_SANITY_CHECKS"
        self.no_allocate=0
        self.bitset = BitSet()
        self.set_bit_int(rhs)

    def set_bit_int(self, rhs):
        if rhs and hasattr(rhs, "__iter__") and not hasattr(rhs[0], "__iter__"):
            for integer in rhs:
                if integer < 0:
                    raise ValueError("Value Can't be Negative")
                self.bitset.add_element(integer)
        else:
            raise NotImplementedError
    
    def __str__(self):
        binary = bin(self.bitset.bitset)
        output = "intbitset(["
        size = len(binary)
        for i in range(2, size):
            if binary[i] == "1":
                normalized_index = i-1
                output += str(size-normalized_index - 2) + ", "
        return output + "])"
    
    def append(self, integer):
        if integer < 0:
            raise ValueError("Value Can't be Negative")
        self.bitset.add_element(integer)

    def delete(self, integer):
        pass

    def intersection(self, other):
        self.bitset.bitset &= other.bitset.bitset

    def union(self, other):
        self.bitset.bitset |= other.bitset.bitset