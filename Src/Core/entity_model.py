from Src.Core.abstract_class import abstract_class


"""
Общий класс для наследования. Содержит стандартное определение: код, наименование
"""
class entity_model(abstract_class):
    __name:str = ""

    """
    Наименование
    """
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        self.__name = value.strip()

  