from product import Product


class Grass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int, country: str, period: str, color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __repr__(self):
        return (
            f'{self.__class__.__name__}("{self.name}",'
            f'"{self.price}", "{self.quantity}", "{self.description}",'
            f'"{self.quantity}", "{self.color}", "{self.country}",'
        )
