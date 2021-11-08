class Abonents:
    def __init__(self, sur, name, pat, dateofbirth, sex, dateofconnection, bal, rate):
        """

        :param sur: surname
        :param name: name
        :param pat: patronymic
        :param dateofbirth: date of birth
        :param sex: gender
        :param dateofconnection: date of connection
        :param bal: balance
        :param rate: rate
        """
        self.sur = sur
        self.name = name
        self.pat = pat
        self.dateofbirth = dateofbirth
        self.sex = sex
        self.dateofconnection = dateofconnection
        self.bal = bal
        self.rate = rate
dimon = Abonents('Блинов', 'Дмитрий', 'Николаевич', '14.05.2003', 'Мужчина', '08.11.2021', '0 рублей',
                    'Таттелеком')
print(dimon.sur)