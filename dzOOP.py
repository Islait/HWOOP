class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += grade
            else:
                lecturer.grades_1[course] = grade
        else:
            return 'Упс'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lecturer(self):
            return super().rate_lecturer
        def rate_hw(self):
            return super().rate_hw

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        #r_2 = 
        return r
        


class Reviewer(Mentor):
    #def __init__(self, name, surname):
        #super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r


Boris = Student('Boris', 'Ivanov', 'man')
mentor_1 = Reviewer('Yana', 'Petrova')
mentor_lectrer = Lecturer('Some', 'Body')
mentor_lectrer_2 = Lecturer('Ben', 'Green')
Boris.courses_in_progress += ['Python']
Boris.courses_in_progress += ['C++']
mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['C++']

mentor_lectrer.courses_attached += ['Python']
mentor_lectrer_2.courses_attached += ['Git']
mentor_1.rate_hw(Boris, 'Python', 10)
mentor_1.rate_hw(Boris, 'Python', 10)
mentor_1.rate_hw(Boris, 'C++', 9)
mentor_1.rate_hw(Boris, 'C++', 8)

Boris.rate_lecturer(mentor_lectrer, 'Python', 10)
Boris.rate_lecturer(mentor_lectrer, 'Python', 10)

print(Boris.grades)
print(mentor_lectrer.grades_1)
print(mentor_1)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += grade
            else:
                lecturer.grades_1[course] = grade
        else:
            return 'Упс'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lecturer(self):
            return super().rate_lecturer
        def rate_hw(self):
            return super().rate_hw

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}
        
    def mid_1(self):
        sum = 1
        for val in self.grades_1.values():
            for v in val:
                sum += int(v)
        self.mid_1 = sum

    
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\n Mid: {self.mid_1()}\nMid {self.mid_1}'
        return r 
        


class Reviewer(Mentor):
    #def __init__(self, name, surname):
        #super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r


Boris = Student('Boris', 'Ivanov', 'man')
mentor_1 = Reviewer('Yana', 'Petrova')
mentor_lectrer = Lecturer('Some', 'Body')



mentor_lectrer.courses_attached += ['Python']

mentor_1.rate_hw(Boris, 'Python', 10)
mentor_1.rate_hw(Boris, 'Python', 10)

Boris.rate_lecturer(mentor_lectrer, 'Python', 10)
Boris.rate_lecturer(mentor_lectrer, 'Python', 10)

print(Boris.grades)
print(mentor_lectrer.grades_1)
print(mentor_1)
print(mentor_lectrer)
#print(mentor_lectrer.sum_1)






class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += grade
            else:
                lecturer.grades_1[course] = grade
        else:
            return 'Упс'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lecturer(self):
            return super().rate_lecturer
        def rate_hw(self):
            return super().rate_hw

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}
        
    def mid_1(self):
        sum = 1
        for val in self.grades_1.values():
            for v in val:
                sum += int(v)
        self.mid_1 = sum

    
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\n Mid: {self.mid_1()}\nMid {self.mid_1}'
        return r 
        


class Reviewer(Mentor):
    #def __init__(self, name, surname):
        #super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r


Boris = Student('Boris', 'Ivanov', 'man')
mentor_1 = Reviewer('Yana', 'Petrova')
mentor_lectrer = Lecturer('Some', 'Body')
mentor_lectrer.mid_1


mentor_lectrer.courses_attached += ['Python']

mentor_1.rate_hw(Boris, 'Python', 10)
mentor_1.rate_hw(Boris, 'Python', 10)

Boris.rate_lecturer(mentor_lectrer, 'Python', 10)
Boris.rate_lecturer(mentor_lectrer, 'Python', 10)

print(Boris.grades)
print(mentor_lectrer.grades_1)
print(mentor_1)
print(mentor_lectrer)
#print(mentor_lectrer.sum_1)



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += [grade]
            else:
                lecturer.grades_1[course] = [grade]
        else:
            return 'Упс'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lecturer(self):
            return super().rate_lecturer
        def rate_hw(self):
            return super().rate_hw

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}
        
    def mid_1(self):
        sum = 0
        count = 0
        for i in self.grades_1.values():
            for j in i:
                sum += j
                count += 1
        return sum/count
         
    
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nMid: {self.mid_1()}\n'
        return r  
        

#Работающий код с средним значением
        
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += [grade]
            else:
                lecturer.grades_1[course] = [grade]
        else:
            return 'Упс'

    def _mid_1(self):
        sum = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                sum += j
                count += 1
        return sum/count

    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self._mid_1(), 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return r

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        n = self._mid_1() > other._mid_1()
        if n == True:
            return f'Средняя оценка выше у {self.name}'
        else:
            return f'Средняя оценка выше у {other.name}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        def rate_lecturer(self):
            return super().rate_lecturer
        def rate_hw(self):
            return super().rate_hw

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}
        
    def _mid_1(self):
        sum = 0
        count = 0
        for i in self.grades_1.values():
            for j in i:
                sum += j
                count += 1
        return sum/count
         
    def __str__(self):
        r = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._mid_1(), 2)}\n'
        return r
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        n = self._mid_1() > other._mid_1()
        if n == True:
            return f'У {self.name} больше'
        else:
            return f'Больше у {other.name}'
        

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
        r = f'Имя: {self.name}\nФамилия: {self.surname}'
        return r


student_1 = Student('student_1', 'Ivanov', 'man')
student_2 = Student('Petr', 'Petrov', 'man')
mentor_1 = Reviewer('Yana', 'Petrova')
mentor_2 = Reviewer('Alex', 'Braun')
mentor_lectrer = Lecturer('Some', 'Body')
mentor_lectrer_2 = Lecturer('Oleg', 'Smirnov')

student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['Git']
mentor_2.courses_attached += ['Git']

mentor_lectrer.courses_attached += ['Python']
mentor_lectrer.courses_attached += ['Git']
mentor_lectrer_2.courses_attached += ['Python']
mentor_lectrer_2.courses_attached += ['Git']

mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_2, 'Python', 10)
mentor_1.rate_hw(student_2, 'Python', 9)
mentor_2.rate_hw(student_1, 'Git', 10)
mentor_2.rate_hw(student_2, 'Git', 9)

student_1.rate_lecturer(mentor_lectrer, 'Python', 10)
student_1.rate_lecturer(mentor_lectrer, 'Python', 10)
student_1.rate_lecturer(mentor_lectrer, 'Git', 10)
student_1.rate_lecturer(mentor_lectrer, 'Git', 10)
student_2.rate_lecturer(mentor_lectrer_2, 'Python', 10)
student_2.rate_lecturer(mentor_lectrer_2, 'Git', 8)

print(student_1.grades)
print(student_2.grades)
print(mentor_lectrer.grades_1)
print(mentor_1)
print(mentor_lectrer)
print(mentor_lectrer_2)
print(student_2)
print(student_1)
print(student_1 < student_2)
print(mentor_lectrer < mentor_lectrer_2)


def average_S(list, name_cource):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades[name_cource]:
            sum += j
            count += 1
    return round(sum/count, 2)

def average_L(list, name_cource):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades_1[name_cource]:
            sum += j
            count += 1
    return round(sum/count, 2)

print(average_S([student_1, student_2], 'Python'))
print(average_L([mentor_lectrer, mentor_lectrer_2], 'Git'))