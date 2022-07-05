class Father:
    def __init__(self) -> None:
        print("I have sperm")
class Mother:
    def __init__(self) -> None:
        print("I have ovary")

class son (Father,Mother):
    def __init__(self) -> None:
        Father.__init__(self)
        Mother.__init__(self)
    def work(self):
        print("I am born")
    
anish = son()
anish.work()