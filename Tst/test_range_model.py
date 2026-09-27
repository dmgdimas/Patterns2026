"""
Автотесты для модели единиц измерения.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.range_model import range_model


class test_range_model:
    """Тесты для модели единицы измерения"""

    def test_success_init_range_model_base_range(self):
        """Проверяет создание базовой единицы измерения (грамм)"""
        base_range = range_model("gram", 1)
        
        assert base_range.name == "gram"
        assert base_range.conversion_factor == 1
        assert base_range.base_range is None

    def test_success_init_range_model_derived_range(self):
        """Проверяет создание производной единицы (кг) на основе базовой"""
        base_range = range_model("gram", 1)
        kg_range = range_model("kg", 1000, base_range)
        
        assert kg_range.name == "kg"
        assert kg_range.conversion_factor == 1000
        assert kg_range.base_range is base_range

    def test_success_convert_to_base_range_model_kg_to_grams(self):
        """Демонстрирует работу пересчета: 2 кг должны дать 2000 грамм"""
        base_range = range_model("gram", 1)
        kg_range = range_model("kg", 1000, base_range)
        
        result = kg_range.convert_to_base(2)
        assert result == 2000.0

    def test_validation_error_set_name_range_model_empty_name(self):
        """Проверяет выброс исключения при пустом наименовании"""
        with pytest.raises(argument_exceptions):
            range_model("", 1)

    def test_validation_error_set_factor_range_model_negative_factor(self):
        """Проверяет выброс исключения при отрицательном коэффициенте"""
        with pytest.raises(argument_exceptions):
            range_model("pcs", -1)









