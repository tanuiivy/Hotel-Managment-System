# main.py

import datetime
from hotel_booking import Room, Guest, Reservation  # Import classes from hotel_booking.py

# Main Program
def main():
    hotel_rooms = []  # A list to store hotel rooms
    guest_name = input("Enter your name: ")
    guest_contact = input("Enter your contact number: ")
    guest = Guest(guest_name, guest_contact)

    while True:
        print("\nMenu:")
        print("1. Add Room")
        print("2. Book Room")
        print("3. Release Room")
        print("4. Show Available Rooms")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                room_number = int(input("Enter room number: "))
                room_type = input("Enter room type: ")
                package_type = input("Enter package type: ")
                price = float(input("Enter room price: "))
                new_room = Room(room_type, room_number, package_type, price)
                hotel_rooms.append(new_room)  # Add the new room to the list
                print(f"Room {room_number} added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values for room number and price.")

        elif choice == "2":
            try:
                room_number = int(input("Enter the room number to book: "))
                check_in_date_str = input("Enter the check-in date (YYYY-MM-DD): ")
                check_out_date_str = input("Enter the check-out date (YYYY-MM-DD): ")
                check_in_date = datetime.datetime.strptime(check_in_date_str, "%Y-%m-%d")
                check_out_date = datetime.datetime.strptime(check_out_date_str, "%Y-%m-%d")
                room = next(r for r in hotel_rooms if r.room_number == room_number)
                guest.book_room(room, check_in_date, check_out_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
            except StopIteration:
                print(f"Room {room_number} does not exist.")

        elif choice == "3":
            try:
                room_number = int(input("Enter the room number to release: "))
                room = next(r for r in hotel_rooms if r.room_number == room_number)
                guest.release_room(room)
            except StopIteration:
                print(f"Room {room_number} does not exist.")

        elif choice == "4":
            for room in hotel_rooms:
                print(room)

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
