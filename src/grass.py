from product import Product


class Grass(Product):
    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 count: int,
                 country: str,
                 period: str,
                 color: str
                 ):
        super().__init__(name, description, price, count)
        self.country = country
        self.period = period
        self.color = color


