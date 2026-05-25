from FrameWorks.MVC import Repository
from FrameWorks.MVC.Mapper import Mapper
from FrameWorks.MVC.Models.Entity import Entity
from FrameWorks.MVC.Models.Footwear import Footwear
from FrameWorks.MVC.Models.FootwearRequest import FootwearRequest
from FrameWorks.MVC.Models.FootwearResponce import FootwearResponse

class Service:
    def __init__(self, repository : Repository):
        self._repository = repository

    def createFootwear(self, footwear: FootwearRequest) -> FootwearResponse:
        footwear_entity = Mapper.map_entity(footwear)
        footwear_entity = self._repository.create(footwear_entity)
        footwear_response = Mapper.map_response(footwear_entity)
        return footwear_response
    
    def readAllFootwear(self) -> list[FootwearResponse]:
        footwear_entities = self._repository.readAll()
        footwear_responses = [Mapper.map_response(entity) for entity in footwear_entities]
        return footwear_responses

    def readFootwear(self, footwear_id: int) -> FootwearResponse:
        footwear_entity = self._repository.read(footwear_id)
        if footwear_entity is None:
            return None
        footwear_response = Mapper.map_response(footwear_entity)
        return footwear_response
    
    def updateFootwear(self, footwear_id: int, footwear: FootwearRequest) -> FootwearResponse:
        footwear_entity = Mapper.map_entity(footwear)
        footwear_entity = self._repository.update(footwear_id, footwear_entity)
        if footwear_entity is None:
            return None
        footwear_response = Mapper.map_response(footwear_entity)
        return footwear_response
    
    def deleteFootwear(self, footwear_id: int) -> bool:
        return self._repository.delete(footwear_id)