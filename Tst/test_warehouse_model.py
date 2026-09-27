"""
Автотесты для модели единиц измерения.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.organization_model import organization_model
from Src.Models.warehouse_model import warehouse_model


class test_warehouse_model:
    """Тесты для модели склада"""

    def test_success_init_warehouse_model_linked_to_organization(self):
        """Проверяет создание склада и его связь с организацией"""
        org = organization_model("1234567890", "044525225", "40817810000000000000", "LLC")
        warehouse = warehouse_model("Main warehouse", org)
        
        assert warehouse.name == "Main warehouse"
        assert warehouse.organization is org

