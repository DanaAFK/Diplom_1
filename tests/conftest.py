import pytest
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient

# Фикстура для создания объекта Bun
@pytest.fixture
def bun_fixture():
    return Bun(name="Classic Bun", price=199)

@pytest.fixture
def ingredient_fixture():
    return Ingredient(ingredient_type="Начинки", name="Биокотлета", price=300)

