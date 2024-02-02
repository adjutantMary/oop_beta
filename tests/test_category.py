import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_products():
    return Category("Напитки", "Здесь находится описание категории", ["молоко", "вода", "вино", "сок"])


@pytest.fixture
def products_():
    return Product("Product3", "Description3", 20.0, 0)


def test_init_category(category_products):
    assert category_products.name == "Напитки"
    assert category_products.description == "Здесь находится описание категории"
    assert category_products.get_products == ["молоко", "вода", "вино", "сок"]


def test_counting(category_products):
    assert len(category_products.get_products) == 4


def test_raises_quantity():
    with pytest.raises(ValueError, match="товар с нулевым количеством не может быть добавлен"):
        product1 = Product("Product1", "Description1", 10.0, 20)
        product2 = Product("Product2", "Description2", 15.0, 30)
        product3 = Product("Product3", "Description3", 20.0, 0)

        category = Category("Category1", "Category Description", [product1, product2])
        category.adding_new_product(product3)
