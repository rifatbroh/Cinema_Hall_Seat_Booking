class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def view_show_list(cls):
        shows = []
        for hall in cls.__hall_list:
            shows.extend(hall.view_show_list())
        return shows


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, ID, movie_name, time):
        self.__show_list.append((movie_name, ID, time))
        # Initialize seats for each show separately
        self.seats[ID] = [['0' for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, row, col):
        if show_id not in self.seats:
            print("\tError: Show ID does not exist.")
            return

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("\tError: Seat is invalid.")
        elif self.seats[show_id][row][col] == 'X':
            print("\tError: Seat is already booked.")
        else:
            self.seats[show_id][row][col] = 'X'
            print(f'\tSeat ({row + 1}, {col + 1}) Booked successfully.')

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("\tError: Show ID does not exist.")
            return

        seat_matrix = self.seats[show_id]
        print("\tAvailable seats:\n")
        for r in range(self.rows):
            print("\t" + "\t".join(f"{seat}" for seat in seat_matrix[r]))


# Example usage with a menu
hall1 = Hall(5, 5, '201')
hall2 = Hall(1, 2, '202')

hall1.entry_show(101, 'The kalo jadu2', '15:00')
hall1.entry_show(102, 'The life of pie', '16:00')
hall2.entry_show(103, 'Bhulbuliaya 3', '20:00')
hall2.entry_show(104, 'The friendship', '10:00')

while True:
    print("\n\tWelcome To SONY_HALL")
    print("\tOnline Ticketing System")
    print("\t=======================")
    print("\n\tSelect an option:")
    print("\t*****************")
    print("\t1. Show The Trending Movie List")
    print("\t2. View Available Seats")
    print("\t3. Want To Book Seats")
    print("\t4. Exit")
    choice = input("\tChoose an option: ")
    
    if choice == '1':
        show_list = Star_Cinema.view_show_list()
        print("\tShow List:")
        for movie, ID, time in show_list:
            print(f'\tMovie Name: {movie}, ID: {ID}, Time: {time}')

    elif choice == '2':
        show_id = int(input("\tEnter show ID: "))
        hall = next((h for h in Star_Cinema._Star_Cinema__hall_list if any(s[1] == show_id for s in h.view_show_list())), None)
        if hall:
            hall.view_available_seats(show_id)
        else:
            print("\tError: Show not found.")

    elif choice == '3':
        show_id = int(input("\tEnter show ID: "))
        hall = next((h for h in Star_Cinema._Star_Cinema__hall_list if any(s[1] == show_id for s in h.view_show_list())), None)
        if hall:
            num_seats = int(input("\tHow many seats do you want to book? "))
            for _ in range(num_seats):
                row = int(input("\tRow: ")) - 1
                col = int(input("\tColumn: ")) - 1
                hall.book_seats(show_id, row, col)
        else:
            print("\tError: Show not found.")

    elif choice == '4':
        print("\tHave a good day! Exiting...")
        break
    else:
        print("\tInvalid option. Please try again.")
