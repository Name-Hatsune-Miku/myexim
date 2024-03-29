class Car:
    def __init__(self, carname, price, type, function):
        self.carname = carname
        self.price = price
        self.type = type
        self.function = function

    def carshow(self):
        print(self.carname + "," + "百米2秒加速" + "," + self.function)


class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buycar(self, car):
        if self.money >= car.price:
            print(self.name + "买了一辆" + car.carname, "价格为" + str(car.price), "车型为" + car.type, "车功能为" + car.function)
            self.money -= car.price
        else:
            print(self.name + "钱不够买车")


car = Car('小米SU7', 120000, 'SUV', '自动驾驶')
user = User('小强', 1000000)
print(car.carshow())
print(user.buycar(car),end="")
