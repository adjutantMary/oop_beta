from product import Product

class Category:
    """
    Класс, определяющий свойства категорий
    """

    category_count = 0
    unique_products = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list,
    ):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        empty_list = []
        for product in products:
            if product not in empty_list:
                Category.unique_products += 1
                empty_list.append(product)

    @property
    def get_products(self):
        """
        Геттер, выводит список товаров
        """
        products = self.__products
        display = []
        for product in products:
            display.append(
                f'Продукт {product["name"]}, ' f'{product["price"]} руб. ' f'Остаток: {product["quantity"]} шт.'
            )
        return display

    def __str__(self):
        return f"Название категории: {self.name}, " f"Количество продуктов: {len(self.__products)} шт"

    def __add__(self, other):
        '''
        Метод для добавления продукта из класса Product в категорию по имени продукта
        :param other: имя продукта
        :return: список
        '''
        if not isinstance(other, Product):
            return ValueError('Объект не принадлежит классу Product')
        return self.__products.append(other.name)




# first_category = Category("Напитки", "Здесь находится описание категории", ["молоко", "вода", "вино", "сок", "молоко"])
#
# second_category = Category("Фрукты", "Здесь находится описание категории", ["яблоки", "mandarin", "apple", "apple"])
# print(first_category)
