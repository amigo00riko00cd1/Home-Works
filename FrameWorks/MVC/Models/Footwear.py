


class Footwear:
    def __init__(self, sex: str, type: str, producer: str, color: str, size: int, price: float):
        self.sex = sex
        self.type = type
        self.producer = producer
        self.color = color
        self.size = size
        self.price = price

    def __str__(self):
        return f"Footwear(sex={self.sex}, type={self.type}, producer={self.producer}, color={self.color}, size={self.size}, price={self.price})"  