import pytest
from src.training import Employee


@pytest.fixture()
def employee_():
    return Employee('Ivan', 'Ivanov', 50_000)


def test_init(employee_):
    assert employee_.name == 'Ivan'


def test_is_work(employee_):
    assert employee_.is_work == False
    employee_.work()
    assert employee_.is_work == True
