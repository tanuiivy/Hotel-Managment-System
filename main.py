import tkinter as tk
from tkinter import messagebox
from guests import Guest  # Importing the Guest class from guests module
from staff import Staff  # Importing the Staff class (if needed in the future)
from reservation import Reservation  # Importing the Reservation class (if needed in the future)
from room import Room  # Importing the Room class

# Sample room data for demonstration
rooms = [
    Room("Deluxe", "101", "Standard", 200),
    Room("Suite", "102", "Premium", 350),
    Room("Economy", "103", "Basic", 150)
]

class HotelManagementApp:
    """
    A class to represent the Hotel Management System GUI.

    Attributes:
        root (tk.Tk): The main window of the GUI.
        guest (Guest): The guest object created when adding a guest.

    Methods:
        add_guest(): Adds a guest and displays a success message.
        make_reservation(): Makes a reservation for the selected room.
    """
    
    def __init__(self, root):
        """
        Initializes the HotelManagementApp.

        Args:
            root (tk.Tk): The main window of the application.
        """
        self.root = root
        self.root.title("Hotel Management System")

        # Frame for guest information
        self.guest_frame = tk.Frame(self.root)
        self.guest_frame.pack(pady=10)

        # Guest name entry
        tk.Label(self.guest_frame, text="Guest Name:").grid(row=0, column=0)
        self.guest_name_entry = tk.Entry(self.guest_frame)
        self.guest_name_entry.grid(row=0, column=1)

        # Contact number entry
        tk.Label(self.guest_frame, text="Contact Number:").grid(row=1, column=0)
        self.contact_number_entry = tk.Entry(self.guest_frame)
        self.contact_number_entry.grid(row=1, column=1)

        # Button to add guest
        tk.Button(self.guest_frame, text="Add Guest", command=self.add_guest).grid(row=2, columnspan=2)

        # Frame for reservation information
        self.reservation_frame = tk.Frame(self.root)
        self.reservation_frame.pack(pady=10)

        # Dropdown for room selection
        tk.Label(self.reservation_frame, text="Select Room:").grid(row=0, column=0)
        self.room_var = tk.StringVar()
        self.room_dropdown = tk.OptionMenu(self.reservation_frame, self.room_var, *[room.room_number for room in rooms])
        self.room_dropdown.grid(row=0, column=1)

        # Check-in date entry
        tk.Label(self.reservation_frame, text="Check-in Date:").grid(row=1, column=0)
        self.check_in_entry = tk.Entry(self.reservation_frame)
        self.check_in_entry.grid(row=1, column=1)

        # Check-out date entry
        tk.Label(self.reservation_frame, text="Check-out Date:").grid(row=2, column=0)
        self.check_out_entry = tk.Entry(self.reservation_frame)
        self.check_out_entry.grid(row=2, column=1)

        # Button to make reservation
        tk.Button(self.reservation_frame, text="Make Reservation", command=self.make_reservation).grid(row=3, columnspan=2)

    def add_guest(self):
        """
        Adds a guest using the information provided in the entry fields.

        Displays a message box to confirm that the guest was added or warns if input is missing.
        """
        name = self.guest_name_entry.get()
        contact = self.contact_number_entry.get()
        if name and contact:
            self.guest = Guest(name, contact)  # Create a new Guest instance
            messagebox.showinfo("Success", f"Guest {name} added!")  # Display success message
            self.guest_name_entry.delete(0, tk.END)  # Clear the entry field
            self.contact_number_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Input Error", "Please enter both name and contact number.")  # Warn user

    def make_reservation(self):
        """
        Makes a reservation for the selected room with check-in and check-out dates.

        Checks if a room and guest are selected, then confirms the reservation and shows a message box.
        """
        room_number = self.room_var.get()  # Get selected room number
        check_in_date = self.check_in_entry.get()  # Get check-in date
        check_out_date = self.check_out_entry.get()  # Get check-out date

        # Find the room object based on the selected room number
        selected_room = next((room for room in rooms if room.room_number == room_number), None)
        if selected_room:
            if hasattr(self, 'guest'):  # Check if a guest has been added
                self.guest.book_room(selected_room, check_in_date, check_out_date)  # Book the room for the guest
                messagebox.showinfo("Reservation", f"Reservation made for {self.guest.name} in Room {room_number}.")
            else:
                messagebox.showwarning("Reservation Error", "Please add a guest first.")  # Warn user if no guest
        else:
            messagebox.showwarning("Room Error", "Selected room not found.")  # Warn if room not found

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = HotelManagementApp(root)  # Initialize the app
    root.mainloop()  # Start the GUI event loop


