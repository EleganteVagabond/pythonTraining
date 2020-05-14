#Student demo class ClassName(object):

class Student:
    """Simple student class to help the developer learn classes in python"""

    def __init__(self, first_name,last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        if courses == None :
            courses = []
        self.courses = courses

    def __str__(self) :
        return f"FN: {self.first_name.capitalize()}, LN : {self.last_name.capitalize()}\
            \n\tEnrolled in : \t{', '.join(map(str.capitalize,self.courses))}"

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"""Student("{self.first_name}","{self.last_name}",{self.courses})"""

    def __eq__(self, other):
        return other != None and (self.first_name==other.first_name and self.last_name==other.last_name)

    def find_in_file(self,filename):
        with open(filename,"r+") as f :
            for line in f.readlines() :
                if line.strip() != "" :
                    stu = Student.decode(line.strip())
                    if self == stu  :
                        return stu
        return None

    def add_to_file(self,filename):
        if self.find_in_file(filename) != None :
            return "Record already exists"
        else :
            with open(filename,"a+") as f :
                f.write(self.encode())
                # f.write("\n")

    def update_courses_in_file(self,filename) :
        lines = []
        updated = False
        found = False
        with open(filename,"r+") as f :
            for line in f.readlines() :
                stu = Student.decode(line.strip())
                if stu == self and stu.courses != self.courses :
                    lines.append(self.encode()+"\n")
                    updated = True
                else:
                    lines.append(line)
        if updated :
            with open(filename,"w") as f_w :
                f_w.writelines(lines)
        return updated

    def encode(self):
        return self.first_name+","+self.last_name+":"+",".join(self.courses)

    @staticmethod
    def decode(line):
        names,courses = line.split(":")
        first_name,last_name=names.split(",")
        courses= courses.rstrip().split(",")
        return Student(first_name,last_name,courses)

    def add_course(self, course):
        if not course in self.courses:
            self.courses.append(course)
        else :
            print(f"{self.first_name} {self.last_name} is already enrolled in {course} ")

    def del_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else :
            print(f"{self.first_name} {self.last_name} is not enrolled in {course} ")

#------------------------------------------
# class inheritance example
class StudentAthlete(Student) :

    def __init__(self,first,last,courses=None,sport=None) :
        super().__init__(first,last,courses)
        self.sport=sport

#------------------------------------------
# drew = Student.decode("andrew,elegante:python,ruby,javascript")
# print(drew.find_in_file("data.txt"))
# drew.add_course("lego_robotics")
# print(drew.update_courses_in_file("data.txt"))
# jo = Student.decode("jo,schmo:python,ruby,javascript")
# print(jo)
# print(jo.add_to_file("data.txt"))


courses_1=['python','rails','javascript']
jane = StudentAthlete("Jane","Doe",courses_1,"Fencing")
print(isinstance(jane,Student))
print(isinstance(jane,StudentAthlete))
# courses_2=['ruby','c','c#']
drew = Student("Drew","Elegante",courses_1)
print(isinstance(drew,StudentAthlete))
# print(drew)
# enc = drew.encode()
# print(enc)
# doppl = Student.decode(enc)
# print("doppl!",doppl)
# print(repr(drew))
# drew.add_course('ruby')
# drew.add_course('rails')
# drew.del_course('c')
# drew.del_course('rails')
# kev = Student("Kevin","Hatcher",courses_2)
# print(kev)
# jorge = Student("Jorge","Ramirez")
# print(jorge)
