class Reservation:
    '''
       This is the reservation class which will hold reservation-making information and methods 
    '''
    def __init__(self, guest_name):
        self.guest_name = guest_name
        self.reservations = []

    # Overloaded method to handle different types of reservations
    def make_reservation(self, nights, room_type="Standard", special_request=None):
        reservation_details = {
            "nights": nights,
            "room_type": room_type,
            "special_request": special_request if special_request else "None"
        }
        # Append the reservation details to the list of reservations
        # allowing us to keep track of the multiple reservations made by the guest
        self.reservations.append(reservation_details)
        print(f"Reservation made for {self.guest_name}: {nights} night(s) in a {room_type} room.")
        if special_request:
            print(f"Special Request: {special_request}")

    def show_reservations(self):
        print(f"\nReservations for {self.guest_name}:")
        for i, res in enumerate(self.reservations, 1):
            print(f"{i}. {res['nights']} night(s) in a {res['room_type']} room. Special Request: {res['special_request']}")
