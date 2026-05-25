
from FrameWorks.MVC.Models.Entity import Entity


class Repository:
    def __init__(self):
        self._data = []
        self._next_id = 1

    def create(self, item : Entity) -> Entity:
        print(f"Creating item: {item.__dict__}")
        item.id = self._next_id
        self._next_id += 1
        self._data.append(item)
        return item
    
    def readAll(self) -> list[Entity]:
        return self._data
    def read(self, item_id: int) -> Entity:
        for item in self._data:
            if item.id == item_id:
                return item
        return None
    
    def update(self, item_id: int, new_item: Entity) -> Entity:
        for index, item in enumerate(self._data):
            if item.id == item_id:
                new_item.id = item_id
                self._data[index] = new_item
                return new_item
        return None

    def delete(self, item_id: int) -> bool:
        item = self.read(item_id)
        if item:
            self._data.remove(item)
            return True
        return False