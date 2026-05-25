from FrameWorks.MVC.Models.Entity import Entity


class FootwearEntity(Entity):
    sex: str
    footwear_type: str
    producer: str
    size: int
    color: str
    price: float
    def __init__(self):
        super().__init__()
        
       