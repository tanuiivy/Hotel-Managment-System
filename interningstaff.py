#since Interning staff is a child of Staff class we have to import the Parent class so as to inherit the attributes
from staff import Staff

# Interning staff class which is a subclass to the staff class
class InterningStaff(Staff):
    '''
       This is the interning staff class which is a subclass to the staff class
       It will hold information in regards to the interning staff in the hotel
       The attributes will also be private to protect the interns information
    '''
    def __init__(self, name, staff_id, gender, mentor, internship_duration):
        # using the super keyword to inherit the attributes of the staff class
        super().__init__(name, staff_id, gender)
        self.__mentor = mentor
        self.__internship_duration = internship_duration

    # accessor methods
    def get_mentor(self):
        return self.__mentor

    def get_internship_duration(self):
        return self.__internship_duration

    def __str__(self):
        return (super().__str__() +
                f", Mentor: {self.__mentor}, Internship duration: {self.__internship_duration} months")

# testing that the inheritance
# intern = InterningStaff("Ivy Tanui", "9087", "Female", "Chef Harrison", 6)
# print(intern)


