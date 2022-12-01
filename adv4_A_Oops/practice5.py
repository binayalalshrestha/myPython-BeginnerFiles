'''
Write a class Train which has methods to book a 
ticket, get status(no of seats) and get fare information
of trains running under Indian railways.
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in this train are {self.seats}")
        
    def fareInfo(self):
        print(f"The price of the ticket is : Rs {self.fare}.")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry this train is full! Kindly try tomorrow!")

intercity = Train("Intercity : 1305", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()