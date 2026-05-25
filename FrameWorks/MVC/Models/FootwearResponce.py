from pydantic import BaseModel

class FootwearResponse(BaseModel):
    id: int | None = None
    sex: str| None = None
    footwear_type: str | None = None
    producer: str | None = None
    size: int | None = None
    color: str | None = None
    price: float | None = None