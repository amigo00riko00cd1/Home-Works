from FrameWorks.MVC.Models.Footwear import Footwear
from FrameWorks.MVC.Models.FootwearRequest import FootwearRequest
from FrameWorks.MVC.Models.FootwearResponce import FootwearResponse
from FrameWorks.MVC.Models.FootwearEntity import FootwearEntity
from FrameWorks.MVC.Models.Entity import Entity

class Mapper:

    @staticmethod
    def map_response(footwear: Entity) -> FootwearResponse:
        responce = FootwearResponse()
        responce.id = footwear.id
        responce.producer = footwear.producer
        responce.sex = footwear.sex
        responce.footwear_type = footwear.footwear_type
        responce.size = footwear.size
        responce.color = footwear.color
        responce.price = footwear.price

        return responce

    @staticmethod
    def map_request(footwear: Entity) -> FootwearRequest:
        request = FootwearRequest()
        request.id = footwear.id
        request.sex = footwear.sex
        request.footwear_type = footwear.footwear_type
        request.size = footwear.size
        request.color = footwear.color
        request.price = footwear.price
        request.producer = footwear.producer
        return request

    @staticmethod
    def map_entity(footwear) -> FootwearEntity:
        entity = FootwearEntity()
        entity.sex = footwear.sex
        entity.footwear_type = footwear.footwear_type
        entity.size = footwear.size
        entity.color = footwear.color
        entity.price = footwear.price
        entity.producer = footwear.producer

        return entity
    
    
       
    
    
        