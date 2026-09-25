"""
Автотесты для моделей данных.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.range_model import range_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.organization_model import organization_model
from Src.Models.warehouse_model import warehouse_model
from Src.Models.nomenclature_model import nomenclature_model


class test_range_model:
    """Тесты для модели единицы измерения"""

    def test_success_init_range_model_base_range(self):
        """Проверяет создание базовой единицы измерения (грамм)"""
        base_range = range_model("gram", 1)
        
        assert base_range.name == "gram"
        assert base_range.conversion_factor == 1
        assert base_range.base_range is base_range

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


class test_organization_model:
    """Тесты для модели организации"""

    def test_success_init_org_model_all_details(self):
        """Проверяет создание организации со всеми полями"""
        org = organization_model("1234567890", "044525225", "40817810000000000000", "LLC")
        
        assert org.inn == "1234567890"
        assert org.bik == "044525225"
        assert org.account == "40817810000000000000"
        assert org.ownership_form == "LLC"


class test_warehouse_model:
    """Тесты для модели склада"""

    def test_success_init_warehouse_model_linked_to_organization(self):
        """Проверяет создание склада и его связь с организацией"""
        org = organization_model("1234567890", "044525225", "40817810000000000000", "LLC")
        warehouse = warehouse_model("Main warehouse", org)
        
        assert warehouse.name == "Main warehouse"
        assert warehouse.organization is org


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