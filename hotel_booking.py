#creating Room class
class Room:
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
    
#creating Guest class
class Guest:
    #constructor
    def __init__(self,name,contact_number):
        self.name=name
        self.contact_number=contact_number
        self.booked_rooms=[]#empty list that will hold booked rooms

    #method on room booking
    def book_room(self, room, check_in_date, check_out_date):
        #creating a condition for determing availability of a room
        if room.check_availability():
            room.book_room(check_in_date, check_out_date)
            self.booked_rooms.append(room)
            #.append()- to add new elements to the end of lists
            print(f"{self.name} booked room {room.room_number} from {check_in_date} to {check_out_date}.")
        else:
            print(f"Room {room.room_number} is not available.")

    #method for releasing a room
    def release_room(self,room):
        if room in self.booked_rooms:
            room.release_room()
            self.booked_rooms.remove(room)
            print(f"{self.name} released room {room.room_number}.")
        else:
            print(f"{self.name} did not book room {room.room_number}.")    
    
    def __str__(self):
        return f"Guest Name: {self.name}, Contact: {self.contact_number}, Rooms Booked: {[room.room_number for room in self.booked_rooms]}"

  