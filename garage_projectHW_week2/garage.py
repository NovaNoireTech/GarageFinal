
class Gargage():
    def __init__(self, num):
        self.tickets = {}
        # self.spots = spots
        # self.rate = rate

        for x in range(1, num +1): 
            self.tickets[x]= {"available": True, "paid" : False}
                
    def take_ticket(self, ticket):
        for space in self.tickets:
            if self.tickets[space]['available'] == True:
                self.tickets[space]['available'] ==False
                print(f"{space} is your ticket number")
                return
            print ("What is your ticket number")
        
    def payForParking(self, ticket):
        if self.tickets[ticket]['available'] == True:
            payment = input("Enter $10 to pay:")
            if payment:
                    print("Your ticket has been paid. You have ten minutes to leave")
                    self.tickets[ticket]['paid'] = True
            else:
                    print("Payment not received. Please pay to exit.")
                        
    def leaveGarage(self, ticket):
        if self.tickets[ticket]['paid'] == True:
            print("Thank you, have a nice day!")
            self.tickets[ticket]['available'] == True
            self.tickets[ticket]['paid'] == False
        else: 
            payment = input ("Please pay before you leave")
            if payment:
                print ("Thank you have a nice day")
                
garage = Gargage (10) 
garage.take_ticket(1)  
garage.payForParking(1) 
garage.leaveGarage(1)