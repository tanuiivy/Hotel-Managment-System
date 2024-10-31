#since Rooms under repair is a child of Room class we have to import the Parent class so as to inherit the attributes
from room import Room
'''
     This is the rooms under repair a child class for the rooms class
     It hold information in regard to the rooms that are being repaired 
     while still inheriting the attributes of it Parent class(room): this is evident using the super key word
'''

#creating subclass to class room for rooms under repair
class RoomsUnderRepair(Room):
    def __init__(self,room_type,room_number,package_type, price, repair_status):
      super().__init__(room_type, room_number, package_type, price)
      self.repair_status = repair_status  # Status on how the repair is going 

    def start_repair(self):
        self.repair_status = "In Repair"
        self.is_available = False
        print(f"Room {self.room_number} is now under repair.")


    def complete_repair(self):
        self.repair_status = "Repair Complete"
        self.is_available = True
        print(f"Room {self.room_number} has completed repairs and is now available.")  

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return (f"Room {self.room_number}: {self.room_type}, Package: {self.package_type}, "
                f"Price: ${self.price}, Repair Status: {self.repair_status}, "
                f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}, Status: {availability}")