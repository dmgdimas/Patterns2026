from Src.Core.entity_model import entity_model
from Src.Core.exceptions import argument_exceptions

class range_model(entity_model):
    """Модель единицы измерения с поддержкой пересчета в базовую единицу"""

    def __init__(self, name:str, conversion_factor:str, base_range:'range_model'=None):
        """
        Инициализирует единицу измерения.
        :param name: Наименование (например, 'кг').
        :param conversion_factor: Коэффициент пересчета в базовую единицу.
        :param base_range: Базовая единица. Если не передана, сущность становится базовой для себя.
        """
        super().__init__()
        self.name = name
        self.conversion_factor = conversion_factor
        self.base_range = base_range
    @property
    def name(self) -> str:
        """Возвращает наименование единицы измерения."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает наименование, проверяя его на пустоту."""
        if not value or not value.strip():
            raise argument_exceptions("Наименование единицы измерения не может быть пустым")
        self.__name = value.strip()

    @property
    def conversion_factor(self) -> float:
        """Возвращает коэффициент пересчета."""
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: float) -> None:
        """Устанавливает коэффициент пересчета (должен быть > 0)."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise argument_exceptions("Коэффициент пересчета должен быть положительным числом")
        self.__conversion_factor = float(value)

    @property
    def base_range(self) -> 'range_model':
        """Возвращает базовую единицу измерения."""
        return self.__base_range

    @base_range.setter
    def base_range(self, value: 'range_model') -> None:
        """Устанавливает базовую единицу измерения."""
        if value is not None and not isinstance(value, range_model):
            raise argument_exceptions("Базовая единица должна быть экземпляром range_model или None")
        self.__base_range = value

    def convert_to_base(self, quantity: float) -> float:
        """
        Пересчитывает заданное количество в базовую единицу измерения.
        :param quantity: Количество в текущих единицах.
        :return: Количество в базовых единицах.
        """
        return quantity * self.conversion_factor