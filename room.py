#creating Room class
class Room:
    '''
       This is the room class that will have attributes
        in regards to the rooms offered in the hotel
       The methods in the class will also be in regards to aspects concerning the room
    '''
    #constructor
    def __init__(self,room_type,room_number,package_type, price):
        self.room_type=room_type
        self.room_number=room_number
        self.package_type=package_type
        self.price=price
        self.is_available =True
        self.check_in_date = None  #default is none until set
        self.check_out_date = None #default is none until set

#methods involved with booking a room
#method checking for room availability
    def check_availability(self):
        return self.is_available

    def book_room(self,check_in_date,check_out_date):
        self.is_available= False
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
#method marking the room as available
    def release_room(self):
        self.is_available=True
        self.check_in_date=None
        self.check_out_date=None
    
    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return (f"Room {self.room_number}: {self.room_type}, Package: {self.package_type}, "
                f"Price: ${self.price}, Check-in: {self.check_in_date}, "
                f"Check-out: {self.check_out_date}, Status: {availability}")
    