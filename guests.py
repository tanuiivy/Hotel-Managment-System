#creating Guest class
class Guest:
    '''
       This is the guest class that will have attributes
        that offer information in regards to the guest coming to the hotel
        The methods below are surronding the booking and releasing of the rooms the guests will use
    '''
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
