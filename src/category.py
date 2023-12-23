
class Category:
    '''
    Сласс, определяющий свойства категорий
    '''

    category_count = 0
    unique_products = 0

    def __init__(
            self,
            name: str,
            description: str,
            products: list
    ):
        self.name = name
        self.description = description
        self.products = products



