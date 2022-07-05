class Human:
    def __init__(self,name,occupatoion):
        self.name = name
        self.occupation = occupatoion
        print("Human Created!!!")
    def do_work(self):
        print(f"Hello there I am {self.name} and I am a(n) {self.occupation} ")

tom = Human("Tom Cruise","actor")
tom.do_work()