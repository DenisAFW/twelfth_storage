# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv
import os.path



class NameValidate:

    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not all(i.isalpha() for i in value.split()):
            raise ValueError("Имя должно содержать только буквыю")
        if not all(i.istitle() for i in value.split()):
            raise ValueError("Имя должно начинаться с заглавной буквы.")
        instance._name = value


class Student:
    name = NameValidate()

    def __init__(self, name, subjects_file):
        self.name = name
        if os.path.exists(subjects_file):
            self.subjects = self.load_sub(subjects_file)
            self.scores = {subject: {"grades": [], "test_results": []} for subject in self.subjects}
        else:
            self.subjects = []
            self.scores = {}

    def load_sub(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def __call__(self, subject, grade, test_result):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не существует в данном курсе')
        if 2 < grade > 5:
            raise ValueError("Оценка варируется строго от 2 до 5 баллов")
        if 0 < test_result > 100:
            raise ValueError("Количество баллов варируется строго от 0 до 100")
        self.scores[subject]["grades"].append(grade)
        self.scores[subject]["test_results"].append(test_result)

    def calc_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не существует в данном курсе')
        test_results = self.scores[subject]["test_results"]
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)

    def calc_average_grade(self):
        total_grades = []
        total_subjects = 0
        for subject in self.subjects:
            total_grades.extend(self.scores[subject]["grades"])
            total_subjects += len(self.scores[subject]["grades"])
        if not total_grades:
            return 0
        return sum(total_grades) / total_subjects


student = Student("Ivan Ivanovich Ivanov", "subjects.csv")
student("Math", 4, 89)
student("Physics", 4, 84)
student("Math", 5, 99)

print("Name", student.name)
print("Subjects:", ', '.join(student.subjects))
print("Матан результаты", student.calc_average_test_score("Math"))
print(student.scores)
# Возможно ли вывести на печать список предметов с оценками также красиво,
# как и просто список предметов хоть это и словарь? Через два астерикса идет вывод ошибки TypeError:
# 'Math' is an invalid keyword argument for print()