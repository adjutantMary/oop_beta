from product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        power: int,
        model: str,
        internal_memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.power = power
        self.model = model
        self.internal_memory = internal_memory
        self.color = color

    def __repr__(self):
        return (
            f'{self.__class__.__name__}("{self.name}",'
            f'"{self.price}", "{self.quantity}", "{self.description}",'
            f'"{self.power}", "{self.model}", "{self.internal_memory}",'
            f'"{self.color}")'
        )
