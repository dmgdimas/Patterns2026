"""
Автотесты для модели группы номенклатуры.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.nomenclature_group_model import nomenclature_group_model


class test_nomenclature_group_model:
    """Тесты для модели группы номенклатуры"""

    def test_success_init_group_model_valid_name(self):
        """Проверяет создание группы с валидным именем"""
        group = nomenclature_group_model("Dairy products")
        assert group.name == "Dairy products"

    def test_validation_error_set_name_group_model_exceeds_limit(self):
        """Проверяет выброс исключения при имени длиннее 50 символов"""
        long_name = "A" * 51
        with pytest.raises(argument_exceptions):
            nomenclature_group_model(long_name)
