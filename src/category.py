from src.product import Product


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
        product_list = self.__products
        display = []
        for product in product_list:
            display.append(
                f'Продукт {product["name"]}, ' f'{product["price"]} руб. ' f'Остаток: {product["quantity"]} шт.'
            )
        return display

    def __str__(self):
        return f"Название категории: {self.name}, " f"Количество продуктов: {len(self.__products)} шт"

    def adding_new_product(self, new_product):
        """
        Метод для добавления продукта из класса Product в категорию по имени продукта
        :param new_product: новый продукт, который добавляется в категорию
        :return: список
        """
        if not isinstance(new_product, Product):
            return ValueError("Объект не принадлежит классу Product")
        elif new_product['quantity'] == 0:
            raise ValueError("товар с нулевым количеством не может быть добавлен")
        return self.__products.append(new_product.name)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}",' f'"{self.description}", "{self.__products}"'

    def average_price_tag(self):
        '''
        Метод для получения среднего ценника за все продукты в категории
        :return:
        '''
        try:

            for

if __name__ == "__main__":
    first_category = Category("Напитки", "Здесь находится описание категории", ["молоко", "вода", "вино", "сок", "молоко"])

    second_category = Category("Фрукты", "Здесь находится описание категории", ["яблоки", "mandarin", "apple", "apple"])
    print(first_category)
