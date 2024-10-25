#creating Staff class
class Staff:
    '''
       This is the staff class that will have attributes
        in regards to the hotel staff.
        The attributs are private for the security of the staff
    '''
    def __init__(self,name,staff_id,gender):
        #making the attributes private
        self.__name=name
        self.__staff_id=staff_id
        self.__gender=gender

    #accessor methods
    def get_name(self):
        return self.__name

    def get_staff_id(self):
        return self.__staff_id

    def get_gender(self):
        return self.__gender
 
    def __str__(self):
        return f"Staff Name: {self.__name}, Staff ID: {self.__staff_id}, Gender: {self.__gender}"
  

