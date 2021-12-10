abitura = []
faculties = []
class Abiturient:
    def __init__(self, name, surname, score, desired_faculty, form_of_education = ''):
        self.score = score
        self.name = name
        self.surname = surname
        self.desired_faculty = desired_faculty
        self.form_of_education = form_of_education
        abitura.append(self)
        abitura.sort(reverse=True, key=lambda self: self.score)



class Faculty:
    def __init__(self, name, university, budget_places, contract_places):
        self.name = name
        self.university = university
        self.budget_places = budget_places
        self.contract_places = contract_places
        faculties.append(self)
        self.received = []
    def accpet_application(self):
        if self.budget_places != 0:
            for i in abitura:
                if i.desired_faculty == self.name and i.form_of_education == '':
                    i.form_of_education = 'бюджет'
                    self.budget_places -= 1
                    self.received.append(i)
                    break
        elif self.contract_places != 0:
            for i in abitura:
                if i.desired_faculty == self.name and i.form_of_education == '':
                    i.form_of_education = 'контракт'
                    self.contract_places -= 1
                    self.received.append(i)
                    break
        else:
            print('Закончились места в институте')
    def print_received(self):
        print('Абитуриенты, поступившие в институт', self.name, ':')
        for i in self.received:
            print(i.name, i.surname, i.score, i.form_of_education)



class University:
    def __init__(self, name, facs = []):
        self.name = name
        self.facs = facs
        for i in faculties:
            if i.university == self.name:
                self.facs.append(i)

    def print_faculties(self):
        for i in self.facs:
            print(i.name)

class Army:
    def __init__(self, name):
        self.name = name
        self.soliders = []
    def autumn_call(self):
        for i in abitura:
            if i.form_of_education == '':
                i.form_of_education = self.name
                self.soliders.append(i)
    def print_soliders(self):
        print('В армию забрали:')
        for i in self.soliders:
            print(i.name, i.surname, i.form_of_education)




itis = Faculty('ИТИС', 'КФУ', 1, 2)
ivmit = Faculty('ИВМИТ', 'КФУ', 2, 1)
kfu = University('КФУ')
army = Army('ВС России')
Abiturient('Азат', 'Абдрахманов', 248, 'ИТИС')
Abiturient('Дмитрий', 'Блинов', 234, 'ИВМИТ')
Abiturient('Нияз', 'Галиахмедов', 233, 'ИТИС')
Abiturient('Радмир', 'Фахретдинов', 270, 'ИТИС')
Abiturient('Кристина', 'Коржуева', 278, 'ИТИС')
Abiturient('Данил', 'Чугунов', 201, 'ИВМИТ')
Abiturient('Владислав', 'Колесников', 228, 'ИВМИТ')
Abiturient('Иван', 'Тверитнев', 1, 'ИВМИТ')
itis.accpet_application()
itis.accpet_application()
itis.accpet_application()
itis.accpet_application()
itis.print_received()
ivmit.accpet_application()
ivmit.accpet_application()
ivmit.accpet_application()
ivmit.accpet_application()
ivmit.print_received()
army.autumn_call()
army.print_soliders()