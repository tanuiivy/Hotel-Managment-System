#creating Room class
class Room:
    #constructor
    def __init__(self,room_type,room_number,package_type, price):
        self.room_type=room_type
        self.room_number=room_number
        self.package_type=package_type
        self.price=price
        