from Src.Core.entity_model import entity_model
from Src.Core.exceptions import argument_exceptions

class organization_model(entity_model):
    """Модель организации (контрагента) для финансового учета."""

    def __init__(self, inn: str, bik: str, account: str, ownership_form: str):
        """Инициализирует организацию с реквизитами."""
        super().__init__()
        self.inn = inn
        self.bik = bik
        self.account = account
        self.ownership_form = ownership_form

    @property
    def inn(self) -> str:
        """Возвращает ИНН организации."""
        return self.__inn

    @inn.setter
    def inn(self, value: str) -> None:
        """Устанавливает ИНН."""
        if not value or not value.strip():
            raise argument_exceptions("ИНН не может быть пустым")
        self.__inn = value.strip()

    @property
    def bik(self) -> str:
        """Возвращает БИК банка."""
        return self.__bik

    @bik.setter
    def bik(self, value: str) -> None:
        """Устанавливает БИК."""
        if not value or not value.strip():
            raise argument_exceptions("БИК не может быть пустым")
        self.__bik = value.strip()

    @property
    def account(self) -> str:
        """Возвращает расчетный счет."""
        return self.__account

    @account.setter
    def account(self, value: str) -> None:
        """Устанавливает расчетный счет."""
        if not value or not value.strip():
            raise argument_exceptions("Расчетный счет не может быть пустым")
        self.__account = value.strip()

    @property
    def ownership_form(self) -> str:
        """Возвращает форму собственности."""
        return self.__ownership_form

    @ownership_form.setter
    def ownership_form(self, value: str) -> None:
        """Устанавливает форму собственности."""
        if not value or not value.strip():
            raise argument_exceptions("Форма собственности не может быть пустой")
        self.__ownership_form = value.strip()