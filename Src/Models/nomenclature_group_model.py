from Src.Core.entity_model import entity_model
from Src.Core.exceptions import argument_exceptions

class nomenclature_group_model(entity_model):
    """Модель группы номенклатуры для объединения товаров."""

    def __init__(self, name: str):
        """Инициализирует группу номенклатуры."""
        super().__init__()
        self.name = name

    @property
    def name(self) -> str:
        """Возвращает наименование группы."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает наименование с ограничением длины до 50 символов."""
        if not value or not value.strip():
            raise argument_exceptions("Наименование группы не может быть пустым")
        if len(value.strip()) > 50:
            raise argument_exceptions("Наименование группы не может превышать 50 символов")
        self.__name = value.strip()