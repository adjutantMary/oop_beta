
class Product:
    '''
    Класс для определения свойств продукта
    '''
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            count: int
    ):
        self.name = name
        self.description = description
        self.price = price
        self.count = count
