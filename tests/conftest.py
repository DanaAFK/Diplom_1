import pytest
from Diplom_1.bun import Bun

# Фикстура для создания объекта Bun
@pytest.fixture
def bun_fixture():
    return Bun(name="Classic Bun", price=1.99)