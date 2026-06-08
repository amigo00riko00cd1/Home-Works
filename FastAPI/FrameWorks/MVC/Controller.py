from FastAPI.FrameWorks.MVC import Service
from FastAPI.FrameWorks.MVC.Models.Footwear import Footwear
from FastAPI.FrameWorks.MVC.Models.FootwearResponce import FootwearResponse
from FastAPI.FrameWorks.MVC.Models.FootwearRequest import FootwearRequest


class Controller:
    def __init__(self, service: Service):
        self._service = service

    def create(self, footwear: FootwearRequest)-> FootwearResponse:
        return self._service.createFootwear(footwear)

    def read(self, footwear_id: int)-> FootwearResponse:
        return self._service.readFootwear(footwear_id)
    
    def readAll(self)-> list[FootwearResponse]:
        return self._service.readAllFootwear() 

    def update(self, footwear_id: int, footwear: FootwearRequest)-> FootwearResponse:
        return self._service.updateFootwear(footwear_id, footwear)

    def delete(self, footwear_id: int)-> bool:
        return self._service.deleteFootwear(footwear_id)