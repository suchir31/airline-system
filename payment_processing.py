from abc import ABC,abstractmethod
class payment_proccesor(ABC):
        def processPayment(self, **kwargs):
            @abstractmethod
            
class stripe_payment(payment_proccesor):
        def processPayment(self,amount,id):
            print(amount,id,"done by stripe")
            
class paypal_payment(payment_proccesor):
        def processPayment(self,amount,id):
            print(amount,id,"done by paypal")
        
class User():
    def __init__(self,name,email):
        self.name=name
        self.email=email
        
class Order():
    def __init__(self):
        
    def 
            

      