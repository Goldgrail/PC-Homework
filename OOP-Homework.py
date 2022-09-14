class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("Оценка должна быть в диапазоне от 1 до 10 баллов")
            elif course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_student_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return round(result, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя Оценка за домашние задания: {self._average_student_grade()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Такого студента нет в списке")
            return
        else:
            return self._average_student_grade() < other._average_student_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return round(result, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя Оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Такого Лектора нет в списке")
            return
        else:
            return self._average_grade() < other._average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ["Введение в програмирование"]

worst_student = Student('Masha', 'Ivanova', 'female')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']
worst_student.finished_courses += ["Englist Language"]

petrov = Reviewer("Ivan", "Petrov")
petrov.courses_attached += ['Python']
pavlov = Reviewer("Igor", "Pavlov")
pavlov.courses_attached += ['Git', 'Python']

petrov.rate_hw(best_student, 'Python', 8)
petrov.rate_hw(best_student, 'Python', 5)
pavlov.rate_hw(worst_student, 'Python', 2)
petrov.rate_hw(worst_student, 'Python', 3)

zubrov = Lecturer("Petr", "Zubrov")
zubrov.courses_attached += ['Python']
zubov = Lecturer("Michael", "Zubov")
zubov.courses_attached += ['Python', 'Git']

best_student.rate_hw(zubrov, "Python", 5)
best_student.rate_hw(zubrov, "Python", 9)
best_student.rate_hw(zubrov, "Python", 8)
best_student.rate_hw(zubov, "Git", 10)
worst_student.rate_hw(zubov, "Git", 7)
worst_student.rate_hw(zubov, "Git", 10)

print(worst_student.grades)
print(worst_student._average_student_grade())
print()
print(best_student)
print()
print(worst_student)
print()
print(petrov)
print()
print(pavlov)
print()
print(zubrov)
print()
print(zubov)
print()
print(zubrov > zubov)
print(best_student > worst_student)


def average_grade_allstudent(student_list, course):
    allgrades = []
    for student in student_list:
        if course in student.grades:
            allgrades += student.grades[course]
    average_result = round(sum(allgrades) / len(allgrades), 2)
    print(f'Cредняя оценка за домашние задания по всем студентам в рамках курса {course}  равна {average_result}')


all_students_list = [best_student, worst_student]
average_grade_allstudent(all_students_list, "Python")


def average_grade_alllecturers(lecturers_list, course):
    allgrades = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            allgrades += lecturer.grades[course]
    average_result = round(sum(allgrades) / len(allgrades), 2)
    print(f'Cредняя оценка за лекции по всем лекторам в рамках курса {course}  равна {average_result}')


all_lecturers_list = [zubrov, zubov]
average_grade_alllecturers(all_lecturers_list, "Python")