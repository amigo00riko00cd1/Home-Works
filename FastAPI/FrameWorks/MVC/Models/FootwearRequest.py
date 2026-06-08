from pydantic import BaseModel

class FootwearRequest(BaseModel):
    sex: str| None = None
    footwear_type: str | None = None
    producer: str | None = None
    size: int | None = None
    color: str | None = None
    price: float | None = None