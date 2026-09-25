from abc import ABC, abstractmethod
import uuid
from Src.Core.exceptions import argument_exceptions

class abstract_class(ABC):
    """
    Абстрактный базовый класс для сотрудника
    Нужен для фиксации ответственного лица при операциях учета (согласно п. 5.3 ТЗ)
    """
    
    def __init__(self):
        """
        Инициализирует экземпляр класса
        """
        # Генерируем уникальный ID с помощью стандартного модуля uuid
        self.__id = str(uuid.uuid4())

    def __eq__(self, other):
        return self.id == other.id


    @property
    def id(self) -> str:
        """Возвращает уникальный ID сотрудника (только для чтения)."""
        return self.__id

    @property
    def name(self) -> str:
        """Возвращает имя сотрудника."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Устанавливает имя, проверяя, что оно не пустое."""
        if not value or not str(value).strip():
            raise argument_exceptions("value","Имя сотрудника не может быть пустым")
        self.__name = str(value).strip()

    @id.setter
    def id(self, value: str):
        """Устанавливает id, проверяя, что оно не пустое."""
        if not value or not str(value).strip():
            raise argument_exceptions("value"," ID сотрудника не может быть пустым")
        self.__id = str(value).strip()
    