class Value:
    def __init__(self):
        self.value = None

    def __set__(self, obj, value):
        self.value = self._commission_value(obj, value)

    def __get__(self, obj, obj_type):
        return self.value

    @staticmethod
    def _commission_value(obj, value):
        return value - value * obj.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


#new_account = Account(0.1)
#new_account.amount = 100

#print(new_account.amount)
