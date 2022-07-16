#constructor
class Ineuron:
    def __init__(self, students, class_fsds, type, number_of_cources):
        self.students = students
        self.class_fsds = class_fsds
        self.type = type
        self.number_of_cources = number_of_cources



a = Ineuron(300, 1, "live_class", 40)
a.students()
a.class_fsds()
a.type()
a.number_of_cources()


#public, private, protected
class Ineuron1:
    def __init__(self, class_type, no_of_cources, affiliates, blog, internship, jobs):
        self._class_type = class_type
        self.no_of_cources = no_of_cources
        self.affiliates = affiliates
        self.blog = blog
        self.internship = internship
        self.__jobs = jobs

a = Ineuron1("data sciece", 2, 10, 50, 20, 1)
print(a._class_type)
print(a._Ineuron1__jobs)


#inheritance
class Ineuron2:
    _class = "live class"
    __class_type = "data science"
    no_of_cources = 1
    internships = "too many"

class Ineuron3(Ineuron2):
    blog = 40
    _jobs = "limited"
    hall_of_fame = 100
    acheivers = "so many"

a = Ineuron3()
print(a)
print(a.acheivers)
print(a.no_of_cources)
print(a.blog)
print(a.hall_of_fame)
print(a.internships)
print(a._class)
print(a._jobs)
print(a._Ineuron2__class_type)


#overriding method
class Ineuron4:
    _class = "live class"
    __class_type = "data science"
    no_of_cources = 1
    internships = "too many"


class Ineuron5(Ineuron4):
    _class = "recorded class"
    __class_type = "oops"
    no_of_cources = 5
    internships = "many"


a = Ineuron5()
print(a._class)
print(a.no_of_cources)
print(a.internships)
print(a._Ineuron5__class_type)

#abstraction
class Ineuron6:
    __blog = "so many"
    def class_type(self):
        print('live class')

    def number_of_cources(self):
        print(10)

    def affiliates(self):
        print(100)

i = Ineuron6()
print(i._Ineuron6__blog)


#encapsulations

class Ineuron7:
    def __init__(self):
        self.__internship = "fsds"

    def students(self):
        print(self.__internship)

    def student_change(self, new_value):
        self.__internship = new_value
i = Ineuron7()
i.students()
i.internship = "python developer"
i.students()
i.student_change("data scientist")
i.students()
