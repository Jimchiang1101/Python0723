class Account:
    __money = 0


    def __init__(self, x) -> None:
        self.__money = x


    def getMoney(self):
        return self.__money


    def save(self, x):
        self.__money += x

    def withdraw(self, x):
        self.__money -= x

    def transfer(self, x, target):
        self.withdraw(x)
        target.save(x)


    def __str__(self) -> str:
        return "帳戶餘額: $" + str(self.__money)