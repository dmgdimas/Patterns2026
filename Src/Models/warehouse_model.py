from Src.Core.entity_model import entity_model
from Src.Core.exceptions import argument_exceptions
from Src.Models.organization_model import organization_model

class warehouse_model(entity_model):
    """Модель склада для учета остатков номенклатуры."""

    def __init__(self, name: str, organization: organization_model):
        """Инициализирует склад, привязанный к организации."""
        super().__init__()
        self.name = name
        self.organization = organization

    @property
    def name(self) -> str:
        """Возвращает наименование склада."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает наименование склада."""
        if not value or not value.strip():
            raise argument_exceptions("Наименование склада не может быть пустым")
        self.__name = value.strip()

    @property
    def organization(self) -> organization_model:
        """Возвращает организацию, которой принадлежит склад."""
        return self.__organization

    @organization.setter
    def organization(self, value: organization_model) -> None:
        """Устанавливает организацию-владельца склада."""
        if not isinstance(value, organization_model):
            raise argument_exceptions("Склад должен быть привязан к организации")
        self.__organization = value