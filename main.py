from datetime import datetime, timedelta

class Room:
    def __init__(self, price, room_number, room_type):
        self.price = price
        self.room_number = room_number
        self.room_type = room_type

class SingleRoom(Room):
    def __init__(self, room_number):
        super().__init__(price=10, room_number=room_number, room_type="Single Room")

class DoubleRoom(Room):
    def __init__(self, room_number):
        super().__init__(price=20, room_number=room_number, room_type="Double Room")

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_booking(self, room_number, date):
        for room in self.rooms:
            if room.room_number == room_number:
                booking = Booking(room, date)
                if date > datetime.now():
                    if not any(booking.date == b.date for b in self.bookings):
                        self.bookings.append(booking)
                        return room.price
                    else:
                        return "There is already a booking for this date"
                else:
                    return "You can only book for future dates"
        return None

    def cancel_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            return True
        else:
            return False

    def list_bookings(self):
        for booking in self.bookings:
            print(
                f'Room Number: {booking.room.room_number}, Price: {booking.room.price}, Room Type: {booking.room.room_type}, Booking Date: {booking.date}')

class Booking:
    def __init__(self, room, date):
        self.room = room
        self.date = date

def initialize_hotel(hotel):
    hotel.add_room(SingleRoom(101))
    hotel.add_room(DoubleRoom(102))
    hotel.add_room(SingleRoom(103))

    hotel.add_booking(room_number=101, date=datetime.now() + timedelta(days=1))
    hotel.add_booking(room_number=102, date=datetime.now() + timedelta(days=2))
    hotel.add_booking(room_number=103, date=datetime.now() + timedelta(days=3))
    hotel.add_booking(room_number=101, date=datetime.now() + timedelta(days=4))
    hotel.add_booking(room_number=102, date=datetime.now() + timedelta(days=5))

def main():
    hotel = Hotel("Hotel")
    initialize_hotel(hotel)

    while True:
        print("\nWhat would you like to do?")
        print("1. Make a booking")
        print("2. Cancel a booking")
        print("3. List bookings")
        print("4. Exit")

        choice = input("Choice: ")

        match choice:
            case "1":
                room_number = int(input("Enter room number: "))
                date_str = input("Enter booking date (YYYY-MM-DD format): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                price = hotel.add_booking(room_number, date)
                if isinstance(price, int):
                    print(f"Booking successful, price: {price}")
                else:
                    print(price)

            case "2":
                print("Please provide booking details:")
                room_number = int(input("Room number: "))
                date_str = input("Date (YYYY-MM-DD format): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                booking = next((b for b in hotel.bookings if b.room.room_number == room_number and b.date == date), None)
                if booking:
                    hotel.cancel_booking(booking)
                    print("Booking canceled.")
                else:
                    print("No such booking found.")

            case "3":
                hotel.list_bookings()

            case "4":
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
