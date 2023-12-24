'''
1 2 3 4 5 6 7 8 9 10 
'''


class train:
    def __init__(self, name ,fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getstatus(self):
        print("**********")
        print(f"the name of the train is {self.name}")
        print(f"the seats available in this train are {self.seats}")
        print("**********")

    def fareInfo(self):
        print(f"the prise of the ticket is : {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket is been booked ! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! kindly try in tatkal")
intercity = train("intercity express 14015",90,300 )
intercity.getstatus()
intercity.bookTicket()
intercity.getstatus()