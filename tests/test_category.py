import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_products():
    return Category("Напитки", "Здесь находится описание категории", ["молоко", "вода", "вино", "сок"])


def test_init_category(category_products):
    assert category_products.name == "Напитки"
    assert category_products.description == "Здесь находится описание категории"
    assert category_products.get_products == ["молоко", "вода", "вино", "сок"]


def test_counting(category_products):
    assert len(category_products.get_products) == 4


# def test_raises_quantity(category_products):
#     prod_ = Product("thing", "text", 100.0, 0)
#     with pytest.raises(ValueError):
#         category_products.append(prod_)
