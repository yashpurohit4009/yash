class marks:
    def data(self):
        self.opt = int(input("theory marks"))
        self.opp = int(input("practical marks"))
        self.opi = int(input("internal marks"))

    def result(self):
        self.total = self.opt + self.opp + self.opi
        return self.total


b2 = marks()
b2.data()
print(b2.result())
        
