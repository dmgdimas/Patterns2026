"""
Модульные тесты для проверки работы абстрактного базового класса.
"""
import pytest
from Src.Core.abstract_class import abstract_class
from Src.Core.exceptions import argument_exceptions


class dummy_entity(abstract_class):
    """
    Фиктивная сущность для тестирования абстрактного класса.
    """

def test_abstract_model_id_not_null():
    """
    Проверяет, что при создании сущности ей присваивается непустой идентификатор.
    """
    entity = dummy_entity()
    assert entity.id != ""
    assert isinstance(entity.id, str)


def test_abstract_model_id_is_unique():
    """
    Проверяет, что каждая новая сущность получает уникальный идентификатор.
    """
    entity1 = dummy_entity()
    entity2 = dummy_entity()
    assert entity1.id != entity2.id


def test_abstract_model_name_is_not_null():
    """
    Проверяет, что попытка установить пустое имя вызывает исключение argument_exceptions.
    """
    entity = dummy_entity()
    with pytest.raises(argument_exceptions):
        entity.name = " "


def test_start():
    """
    Базовый тест-заглушка для проверки работоспособности окружения pytest.
    """
    assert 1 == 1