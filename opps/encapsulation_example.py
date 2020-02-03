class Customer:
    c_bank_name = "SBI"

    def __init__(self, c_name, c_add, c_cno, c_bal):
        self.c_name = c_name
        self.c_add = c_add
        self.c_cno = c_cno
        self.c_bal = c_bal

    def deposit(self, d_amt):
        self.c_bal = self.c_bal + d_amt

    def with_draw(self, w_amt):
        self.c_bal = self.c_bal - w_amt

    def display(self):
        print(self.c_name)
        print(self.c_add)
        print(self.c_cno)
        print(self.c_bal)


c1_ = Customer('peter', "Bhopal", 8225801511, 20000)
c1_.deposit(500)
c1_.with_draw(1000)
c1_.display()

c2_ = Customer('ahmad', 'new_york', 9258465210, 100000)
c2_.deposit(5000)
c2_.with_draw(30000)
c2_.display()



