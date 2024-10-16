import pytest
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.burger import Burger

@pytest.fixture
def bun_fixture():
    return Bun(name="Classic Bun", price=199)

@pytest.fixture
def ingredient_fixture():
    return Ingredient(ingredient_type="Начинки", name="Биокотлета", price=300)

@pytest.fixture
def burger_fixture(bun_fixture, ingredient_fixture):
    burger = Burger()
    burger.set_buns(bun_fixture)
    burger.add_ingredient(ingredient_fixture)
    return burger
