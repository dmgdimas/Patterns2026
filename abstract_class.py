from abc import ABC, abstractmethod
import uuid

class Employee(ABC):
    """
    Абстрактный базовый класс для сотрудника
    Нужен для фиксации ответственного лица при операциях учета (согласно п. 5.3 ТЗ)
    """
    
    def __init__(self, name: str):
        # Генерируем уникальный ID с помощью стандартного модуля uuid
        self.__id = str(uuid.uuid4())
        self.name = name  # Используем сеттер для проверки имени

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
            raise ValueError("Имя сотрудника не может быть пустым")
        self.__name = str(value).strip()

    @abstractmethod
    def get_role(self) -> str:
        """
        Абстрактный метод. 
        Любой наследник этого класса обязан реализовать его и вернуть свою роль 
        (например: "Производство", "Обслуживание", "Управление").
        """
        pass