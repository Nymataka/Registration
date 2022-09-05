from simpletk import *
from student import *
import tkinter as tk
import tkinter.ttk as ttk


class Students(TApplication):  # класс студента
    cheking = 'Данные не введены'
    money_value = 0
    numb = 0
    fullname = ''
    long = 210
    list_s = [[]]

    def __init__(self, title):  # окно студента
        TApplication.__init__(self, title)
        stile = ("MS Sans Serif", 12)
        self.size = (355, 440)
        self.position = (810, 290)
        self.resizable = (False, False)
        self.panel = TPanel(self, relief="raised", height=45, bd=1)
        self.panel.align = "top"
        self.check = TButton(self.panel, text="Проверить", font=stile)
        self.check.position = (5, 5)
        self.check.onClick = self.man
        self.result_of_checking = TLabel(self.panel, text=self.cheking, font=stile)
        self.result_of_checking.position = (105, 7)
        self.name = TLabel(self, text="Имя:", font=stile)
        self.name.position = (5, 100)
        self.input_name = TEdit(self, font=stile, width=self.long)
        self.input_name.position = (130, 100)
        self.surname = TLabel(self, text="Фамилия:", font=stile)
        self.surname.position = (5, 150)
        self.input_surname = TEdit(self, font=stile, width=self.long)
        self.input_surname.position = (130, 150)
        self.patronymic = TLabel(self, text="Отчество:", font=stile)
        self.patronymic.position = (5, 200)
        self.input_patronymic = TEdit(self, font=stile, width=self.long)
        self.input_patronymic.position = (130, 200)
        self.dob = TLabel(self, text="Дата рождения:", font=stile)
        self.dob.position = (5, 250)
        self.input_dob = TEdit(self, font=stile, width=self.long)
        self.input_dob.position = (130, 250)
        self.input_dob.text = "2000.01.01"
        self.gender = TLabel(self, text="Пол:", font=stile)
        self.gender.position = (5, 300)
        self.gender_option = TComboBox(self, values=["м", 'ж'], width=self.long, state="readonly")
        self.gender_option.position = (130, 300)
        self.early = TButton(self, text="<", font=stile)
        self.early.position = (15, 50)
        self.early.onClick = self.early_button
        self.next = TButton(self, text=">", font=stile)
        self.next.position = (316, 50)
        self.next.onClick = self.next_button
        self.student = TLabel(self, text=f'Студент {self.numb + 1}', font=stile)
        self.student.position = (140, 55)
        self.stipend = TLabel(self, text="Стипендия:", font=stile)
        self.stipend.position = (5, 350)
        self.change_money = TTrackBar(self, [0, 5000], width=10, length=self.long, orient=HORIZONTAL, onTrack=self.result)
        self.change_money.position = (130, 340)
        self.change_money.value = 0
        self.money_value = self.change_money.value
        self.finish = TButton(self, text="Готово", font=stile)
        self.finish.position = (150, 390)
        self.finish.onClick = self.end

    def result(self, event=None):  # полоска стипендии
        self.money_value = self.change_money.value

    def man(self, sender):  # создание и проверка студента
        self.fullname = f'{self.input_name.text} {self.input_surname.text} {self.input_patronymic.text}'
        self.list_s[self.numb] = (Student(self.fullname, self.input_dob.text, self.gender_option.text, self.numb,
                                          str(self.money_value)))
        self.list_s[self.numb].chek()
        if self.list_s[self.numb].error == '':
            self.cheking = 'Правильно'
        else:
            self.cheking = self.list_s[self.numb].error
        self.result_of_checking.text = self.cheking

    def next_button(self, sender):  # проверка для продолжения
        try:
            self.list_s[self.numb].chek()
        except:
            pass
            return
        if self.numb + 1 == len(self.list_s):  # показать уже существующего или создать нового
            if self.list_s[self.numb].error == '':
                self.next_st()
            return
        else:
            if self.list_s[self.numb].error == '':
                self.numb += 1
                self.early_st()

    def next_st(self):  # кнопка следующий
        self.numb += 1
        self.input_name.text = ''
        self.input_surname.text = ''
        self.input_patronymic.text = ''
        self.input_dob.text = '2000.01.01'
        self.gender_option.text = ''
        self.cheking = 'Данные не введены'
        self.result_of_checking.text = self.cheking
        self.fullname = ''
        self.list_s.append('')
        self.student.text = f'Студент {self.numb + 1}'
        self.change_money.value = 0
        return

    def early_button(self, sender):  # проверка для продолжения
        if self.numb > 0 and self.cheking == 'Правильно':
            self.numb -= 1
            self.early_st()

    def early_st(self):  # кнопка предыдущий
        self.cheking = 'Правильно'
        self.result_of_checking.text = self.cheking
        self.fullname = ''
        self.input_name.text = self.list_s[self.numb].full_name[0]
        self.input_surname.text = self.list_s[self.numb].full_name[1]
        self.input_patronymic.text = self.list_s[self.numb].full_name[2]
        self.input_dob.text = self.list_s[self.numb].durn_date
        self.gender_option.text = self.list_s[self.numb].gender
        self.change_money.value = self.list_s[self.numb].stipend
        self.student.text = f'Студент {self.numb + 1}'
        return

    def end(self, sender):  # завершить ввод данных
        if self.cheking == 'Правильно':
            self.destroy()
            app = Application(tk.Tk(), self.list_s)
            self.list_s = []
            app.root.mainloop()


class Application(tk.Frame):  # таблица студентов
    def __init__(self, root, s_list):
        self.root = root
        self.s_list = s_list
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.id = 1
        self.iid = 1
        self.numb_s = []
        self.tree = ttk.Treeview(self.root, columns=('Имя', 'Фамилия', 'Отчество', 'Возраст', 'Пол',
                                                     'Стипендия'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Имя')
        self.tree.heading('#2', text='Фамилия')
        self.tree.heading('#3', text='Отчество')
        self.tree.heading('#4', text='Возраст')
        self.tree.heading('#5', text='Пол')
        self.tree.heading('#6', text='Стипендия')
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        self.tree.column('#4', stretch=tk.YES)
        self.tree.column('#5', stretch=tk.YES)
        self.tree.column('#6', stretch=tk.YES)
        self.tree.grid(row=1, columnspan=8, sticky='nsew')
        self.treeview = self.tree
        for i in range(len(self.s_list)):
            self.treeview.insert('', 'end', iid=self.iid, text=f"Студент {str(self.id)}",
                                 values=(self.s_list[i].full_name[0], self.s_list[i].full_name[1],  self.s_list[i].
                                         full_name[2], self.s_list[i].age, self.s_list[i].gender, self.s_list[i].
                                         stipend))
            self.numb_s.append(self.id)
            self.iid = self.iid + 1
            self.id = self.id + 1
        self.root.title("Таблица студентов")


s = Students("Студенты")
s.run()
