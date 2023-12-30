
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

    @staticmethod
    def create_product() -> dict:
        new_product = {'name': 'name_',
                       'description': 'description_',
                       'price': 1000.0,
                       'count': 12}
        return new_product

    @property
    def change_price(self) -> float:
        '''
        Геттер для атрибута цены price
        '''
        return self.price

    @change_price.setter
    def change_price(self, new_price: float):
        '''
        Сеттер для установки новой цены товара
        '''

        if self.price > new_price:
            user_input = input('Если вы хотите изменить стоимость товара, то введите "y",'
                               'Если вы не желаете изменять стоимость, введите "n"')
            if user_input == 'y':
                self.price = new_price
        else:
            self.price = new_price


