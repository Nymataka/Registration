from datetime import datetime


class Student:
    date = str(datetime.now().date()).split('-')  # текущия дата
    day_in_dob, day_in_date, age, error, durn_date = 0, 0, 0, '', ''

    def __init__(self, full_name, dob, gender, number, stipend):  # фио, дата рождения, пол, номер в списке, стипендия
        self.full_name = full_name.split()
        self.dob = str(dob).split('.')
        self.gender = gender
        self.number = number
        self.stipend = stipend

    def chek(self):  # проверка данных
        self.error = ''
        if len(self.full_name) != 3:  # в фио 3 слова
            self.error = 'ФИО введено неверно'
            return
        for alpha in self.full_name:  # в фио нет цифр
            if not alpha.isalpha():
                self.error = 'ФИО введено неверно'
                return
        if len(self.dob) != 3:  # в дате введено 3 числа или неправильный формат
            self.error = 'Дата рождения введена неверно'
            return
        for digit in self.dob:  # в дате нет букв
            if not digit.strip().isdigit():
                self.error = 'Дата рождения введена неверно'
                return
        if (int(self.date[0]) < int(self.dob[0])) or (int(self.dob[0]) < 1000) or \
                (12 < int(self.dob[1])) or (int(self.dob[1]) < 1) or \
                (31 < int(self.dob[2])) or (int(self.dob[2]) < 1):  # указаны существующие даты
            self.error = 'Дата рождения введена неверно'
            return
        self.day_in_date = int(self.date[0]) * 365 + int(self.date[1]) * 30 + int(self.date[2])
        self.day_in_dob = int(self.dob[0]) * 365 + int(self.dob[1]) * 30 + int(self.dob[2])
        self.age = (self.day_in_date - self.day_in_dob) // 365
        if self.age < 0:  # человек родился
            self.error = 'Дата рождения введена неверно'
            return
        self.durn_date = f'{self.dob[0]}.{self.dob[1]}.{self.dob[2]}'
        if self.gender != 'м' and self.gender != 'ж':  # указан существующий пол
            self.error = 'Пол введен неверно'
            return
