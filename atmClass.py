class ATM(object):
    def __init__(self, deposit, widraw, compony, Balance_Enquiry):
        self.widraw = widraw
        self.deposit = deposit
        self. compony = compony
        self.Balance_Enquiry = Balance_Enquiry
    
    def start(self):
        print("Started")
        print("High")
    
    def stop(self):
        print("Stopped")
    
    def accelerate(self):
        print("Accelerating")

    def changeGear(self, gear_type):
        print("Gear Changed")

Samyak = ATM(30000, 100000, "HDFC", 80000000)
print(Samyak.start())
print(Samyak.deposit())