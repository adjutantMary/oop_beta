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
            display.append(product)
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
        elif new_product.quantity == 0:
            raise ValueError("товар с нулевым количеством не может быть добавлен")
        return self.__products.append(new_product.name)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}",' f'"{self.description}", "{self.__products}"'

    def average_price_tag(self):
        """
        Метод для получения среднего ценника за все продукты в категории
        :return: int
        """
        try:
            all_price = 0
            for product in self.__products:
                if product.price:
                    all_price += product
            avg_price = all_price / len(self.__products)
            return avg_price
        except AttributeError:
            print("В данной категории не существует такого продукта")
        except ZeroDivisionError:
            print('Деление на ноль невозможно')
            return 0
