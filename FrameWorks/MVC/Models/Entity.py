class Entity:
    def __init__(self):
        self.id = 0

    def __eq__(self, other):
        if isinstance(other, Entity):
            return self.id == other.id
        return False
    
    def __neq__(self, other):
        return not self.__eq__(other)