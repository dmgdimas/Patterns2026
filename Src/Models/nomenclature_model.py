from Src.Core.entity_model import entity_model
from Src.Core.exceptions import argument_exceptions
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.range_model import range_model

class nomenclature_model(entity_model):
    """Модель номенклатуры (товара/сырья) для складского учета."""

    def __init__(self, name: str, full_name: str, group: nomenclature_group_model, range: range_model):
        """Инициализирует номенклатуру с группой и единицей измерения."""
        super().__init__()
        self.name = name
        self.full_name = full_name
        self.group = group
        self.range = range

    @property
    def name(self) -> str:
        """Возвращает краткое наименование номенклатуры."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает краткое наименование (макс. 50 символов)."""
        if not value or not value.strip():
            raise argument_exceptions("Краткое наименование не может быть пустым")
        if len(value.strip()) > 50:
            raise argument_exceptions("Краткое наименование не может превышать 50 символов")
        self.__name = value.strip()

    @property
    def full_name(self) -> str:
        """Возвращает полное наименование номенклатуры."""
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        """Устанавливает полное наименование (макс. 255 символов)."""
        if not value or not value.strip():
            raise argument_exceptions("Полное наименование не может быть пустым")
        if len(value.strip()) > 255:
            raise argument_exceptions("Полное наименование не может превышать 255 символов")
        self.__full_name = value.strip()

    @property
    def group(self) -> nomenclature_group_model:
        """Возвращает группу номенклатуры."""
        return self.__group

    @group.setter
    def group(self, value: nomenclature_group_model) -> None:
        """Устанавливает группу номенклатуры."""
        if not isinstance(value, nomenclature_group_model):
            raise argument_exceptions("Номенклатура должна быть привязана к группе")
        self.__group = value

    @property
    def range(self) -> range_model:
        """Возвращает единицу измерения номенклатуры."""
        return self.__range

    @range.setter
    def range(self, value: range_model) -> None:
        """Устанавливает единицу измерения."""
        if not isinstance(value, range_model):
            raise argument_exceptions("Номенклатура должна иметь единицу измерения")
        self.__range = value