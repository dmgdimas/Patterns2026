"""
Автотесты для модели организаций.
Проверяют корректное создание моделей и обработку ошибок валидации.
"""
import pytest

from Src.Core.exceptions import argument_exceptions
from Src.Models.organization_model import organization_model



class test_organization_model:
    """Тесты для модели организации"""

    def test_success_init_org_model_all_details(self):
        """Проверяет создание организации со всеми полями"""
        org = organization_model("1234567890", "044525225", "40817810000000000000", "LLC")
        
        assert org.inn == "1234567890"
        assert org.bik == "044525225"
        assert org.account == "40817810000000000000"
        assert org.ownership_form == "LLC"


