class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.index = -1

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n   

    def pushback(self, n: int) -> None:
        if self.index + 1 >= len(self.array):
            self.resize()
        self.index += 1
        self.array[self.index] = n

    def popback(self) -> int:
        self.index -= 1
        return self.array[self.index + 1]

    def resize(self) -> None:
        self.array = self.array + [0] * len(self.array)

    def getSize(self) -> int:
        return self.index + 1
    
    def getCapacity(self) -> int:
        return len(self.array)
