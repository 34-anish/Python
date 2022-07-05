class vehicle:
    def __init__(self) -> None:
        print("The main purpose of the vehicle is the transportaion")
    
class bike(vehicle):
    def __init__(self) -> None:
        print("Bike")
        self.wheels = 2

    def work(self):
        super().__init__()
        print(f"I have {self.wheels} wheels")

kawasaki = bike()
kawasaki.work()



