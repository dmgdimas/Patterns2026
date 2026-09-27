"""
Автотесты для модели номенклатуры.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.range_model import range_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.nomenclature_model import nomenclature_model


class test_nomenclature_model:
    """Тесты для модели номенклатуры"""

    def test_success_init_nomenclature_model_full_parameters(self):
        """Проверяет создание номенклатуры со всеми зависимостями"""
        group = nomenclature_group_model("Milk")
        range = range_model("liter", 1)
        item = nomenclature_model("Milk 3.2%", "Cow milk pasteurized 3.2%", group, range)
        
        assert item.name == "Milk 3.2%"
        assert item.full_name == "Cow milk pasteurized 3.2%"
        assert item.group is group
        assert item.range is range

    def test_validation_error_set_full_name_nomenclature_model_exceeds_255_chars(self):
        """Проверяет выброс исключения при полном имени длиннее 255 символов"""
        group = nomenclature_group_model("Group")
        range = range_model("pcs", 1)
        long_full_name = "B" * 256
        
        with pytest.raises(argument_exceptions):
            nomenclature_model("Test", long_full_name, group, range)

    def test_validation_error_set_name_nomenclature_model_exceeds_50_chars(self):
        """Проверяет выброс исключения при кратком имени длиннее 50 символов"""
        group = nomenclature_group_model("Group")
        range = range_model("pcs", 1)
        long_short_name = "C" * 51
        
        with pytest.raises(argument_exceptions):
            nomenclature_model(long_short_name, "Full name", group, range)