
class Colors:
    def __init__(self, name, r ,g ,b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return(self.r == other.r and
                   self.g == other.g and
                   self.b == other.b)
        return NotImplemented

blue = Colors ("голубой", 255, 0, 0)
black = Colors ("черный", 0, 255, 0)
otherBlue = Colors ("другой голубой", 255, 0, 0)

print(blue == otherBlue)
print(blue)


class People:
    ruClassName = "Человек"
    objInstancesCount = 0

    def __init__(self, name, id, age):
        self._name = name
        self.id = id
        self.age = age
        People.objInstancesCount = People.objInstancesCount + 1

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def info(self):
        print(self._name)
        print("Номер телефона: " + str(self.id))
        print("Возраст: " + str(self.age))

b = People("Патрик", 8924353445, 21)
print("Это " + b.get_name())
b.set_name("Петр")
print("А, нет... Это " + b.get_name())