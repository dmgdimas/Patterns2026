class argument_exceptions(Exception):
    __stack_trace:str = ""
    __message:str = ""

    def __init__(self, message="", stack_trace = ""):
        self.__message = message.strip()
        self.__stack_trace = stack_trace.strip()

    def __str__(self):
        return f"Ошибка: Некорректный аргумент!\n{self.__message}\n{self.__stack_trace}"