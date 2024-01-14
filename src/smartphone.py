from product import Product


class Smartphone(Product):
    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 count: int,
                 power: int,
                 model: str,
                 internal_memory: int,
                 color: str
                 ):
        super().__init__(name, description, price, count)
        self.power = power
        self.model = model
        self.internal_memory = internal_memory
        self.color = color
