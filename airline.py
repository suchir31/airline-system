from abc import ABC,abstractmethod
class Ticket():
    def __init__(self,id,user):
        self.id=id
        self.user=user

class seating_type():
    def __init__(self,type,cost,capacity,airplane_id):
        self.type=type
        self.cost=cost
        self.capacity=capacity
        self.available_seats = capacity
        self.airplane_id=airplane_id
    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

class Trip():
    def __init__(self,airplane_id,arrival,departure,pilot):
        self.airplane_id=airplane_id
        self.arrival=arrival
        self.departure=departure
        self.pilot=pilot
    
class airplane():
    def __init__(self,id,name,seating_types,stops):
        self.name=name
        self.id=id
        self.seating_types=seating_types
        self.stops=stops
        
    def book_ticket(self,seat_type):
        if seat_type in self.seating_types:
             seat_type.book_seat()

class airport():
    def __init__(self,location,air_id):
        self.id=air_id
        self.location=location
        self.airplanes=[]
        
    def add_airplanes(self,airplane):
        self.airplanes.append(airplane)
       
    def show_list(self):
        for airplane in self.airplanes:
            print(airplane)
        
        
class User():
    def __init__(self,name,email,mobile_no):
        self.name=name
        self.email=email
        self.mobile_no=mobile_no
        self.wishlist=[]
        self.past_purchases=[]
        
    
    def make_purchase(self,payment_method,amount,id):
        purchase=payment_method(amount,id)
        if purchase:
            self.past_purchases.append(purchase)
    
    def request_refund(self,ticket_id,reason):
        ProcessRefund(ticket_id,self,reason)
        ProcessRefund.process
    
    def add_to_wishlist(self,airplane):
        self.wishlist.append(airplane)
    
class pilot():
    def __init__(self,name,email,age_exp):
        self.name=name
        self.email=email
        self.age_exp=age_exp
        
class purchase():
    def __init__(self,user,payment_method,amount,purchase_id):
        self.user=user
        self.payment_method=payment_method
        self.amount=amount
        self.purchase_id=purchase_id
        
    def gen_ticket(self,id):
        if self.payment_method().payment(self.amount):
            ticket=Ticket(id,self.user)
            return ticket
        
class process_Payemnt(ABC):
    @abstractmethod 
    def payment(self,amount,id):
       pass
    
   
class stripe_payment(process_Payemnt):
     def payment(self, amount, id):
         print("process payment via stripe_payment")
        
class upi_payment(process_Payemnt):
     def payment(self, amount, id):
         print("process payment via upi_payment")
  
class ProcessRefund():
    def __init__(self,ticket_id,user,reason):
        self.ticket_id=ticket_id
        self.user=user
        self.reason=reason
        self.status="pending"
        
    def process(self):
         pass
        
class NotificationSystem(ABC):
    @abstractmethod
    def notify(self,email,number):
        pass
class NotifyviaSms(NotificationSystem):
     def notify(self, email, number):
         print("notified via sms")
class Notifyviaemail(NotificationSystem):
     def notify(self, email, number):
         print("notified via email")
    
    
        