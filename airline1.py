from abc import ABC, abstractmethod

# Ticket Class
class Ticket:
    def __init__(self, ticket_id, user):
        self.ticket_id = ticket_id
        self.user = user
 
# Seating Type Class
class SeatingType:
    def __init__(self, seat_type, cost, capacity, airplane_id):
        self.seat_type = seat_type
        self.cost = cost
        self.capacity = capacity
        self.available_seats = capacity
        self.airplane_id = airplane_id

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

# Trip Class
class Trip:
    def __init__(self, airplane_id, arrival, departure):
        self.airplane_id = airplane_id
        self.arrival = arrival
        self.departure = departure

# Airplane Class
class Airplane:
    def __init__(self, name, seating_types, stops):
        self.name = name
        self.seating_types = seating_types  # List of SeatingType objects
        self.stops = stops

    def book_ticket(self, seat_type_name):
        for seat in self.seating_types:
            if seat.seat_type == seat_type_name:
                return seat.book_seat()
        return False  # No matching seat type found

# Airport Class
class Airport:
    def __init__(self, location):
        self.location = location
        self.airplanes = []

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)

    def show_airplanes(self):
        for airplane in self.airplanes:
            print(airplane.name)

# Purchase Class
class Purchase:
    def __init__(self, user, payment_method, amount, purchase_id):
        self.user = user
        self.payment_method = payment_method  # Instance of PaymentProcessor subclass
        self.amount = amount
        self.purchase_id = purchase_id

    def generate_ticket(self, ticket_id):
        if self.payment_method.process_payment(self.amount, self.purchase_id):
            return Ticket(ticket_id, self.user)
        return None

# User Class
class User:
    def __init__(self, name, email, mobile_no):
        self.name = name
        self.email = email
        self.mobile_no = mobile_no
        self.wishlist = []
        self.past_purchases = []

    def make_purchase(self, payment_method, amount, purchase_id):
        purchase = Purchase(self, payment_method, amount, purchase_id)
        ticket = purchase.generate_ticket(purchase_id)
        if ticket:
            self.past_purchases.append(ticket)
            return ticket
        return None

    def request_refund(self, ticket_id):
        ProcessRefund(ticket_id)

    def add_to_wishlist(self, airplane):
        self.wishlist.append(airplane)

    def notify(self, msg):
        print(f"Notification for {self.name}: {msg}")

# Abstract Payment Processor
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, transaction_id):
        pass

# Stripe Payment Implementation
class StripePayment(PaymentProcessor):
    def process_payment(self, amount, transaction_id):
        print(f"Processing payment via Stripe: Amount={amount}, Transaction ID={transaction_id}")
        return True  # Assume successful payment

# UPI Payment Implementation
class UpiPayment(PaymentProcessor):
    def process_payment(self, amount, transaction_id):
        print(f"Processing payment via UPI: Amount={amount}, Transaction ID={transaction_id}")
        return True  # Assume successful payment

# Abstract Notification System
class NotificationSystem(ABC):
    @abstractmethod
    def notify(self, email, number):
        pass

# SMS Notification
class NotifyViaSms(NotificationSystem):
    def notify(self, email, number):
        print(f"Notification sent via SMS to {number}")

# Email Notification
class NotifyViaEmail(NotificationSystem):
    def notify(self, email, number):
        print(f"Notification sent via Email to {email}")
