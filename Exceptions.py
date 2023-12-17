class CalcError(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def ret_wrong_input():
        return "Проверьте правильно ли выполнен ввод. Исходная строка "
