
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

        Category.category_count += 1

        empty_list = []
        for product in products:
            if product not in empty_list:
                Category.unique_products += 1
                empty_list.append(product)


first_category = Category(
    'Напитки',
    'Здесь находится описание категории',
    ['молоко', 'вода', 'вино', 'сок', 'молоко'])

second_category = Category(
    'Фрукты',
    'Здесь находится описание категории',
    ['яблоки', 'mandarin', 'apple', 'apple']
)
