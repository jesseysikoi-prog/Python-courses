class Computer:
    def __init__(self):
        self.__price = 9000
    def sell(self):
        print("Selling Price: {}".format(self.__price))
    def setMaxPrice(self, price):
        self.__price = price
c = Computer()
c.sell()
c.___maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()