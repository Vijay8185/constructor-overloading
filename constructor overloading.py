class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Name = {}, Age = {}".format(self.name,self.age)
if __name__ == '__main__':
    studentObj = Student("Aseet",12)
    print(studentObj)

class Series:
    def __init__(self, *args):
        if len(args) == 2:
            self.firstTerm, self.difference = args[0], args[1]

        elif len(args) == 1:
            self.firstTerm, self.difference = args[0], 0
        else:
            self.firstTerm, self.difference = 0, 0

    def NthTerm(self, N):
        return self.firstTerm + (N-1) * self.difference

series1 = Series(10,12)
series2 = Series(10)
series3 = Series(0)


class Triangle:
    def __init__(self, a, b, c):
        # Constructor is called when the object is initialized with required parameters.
        self.a, self.b, self.c = a, b, c

    @classmethod
    def fromString(cls, var):
        # Class method to create object when input is a string
        a, b, c = map(int, var.split())
        # Split the string into numbers and return a new instance.
        return cls(a, b, c)

    @classmethod
    def fromList(cls, lst):
        # Class method to create object when input is list
        a, b, c = lst[0], lst[1], lst[2]
        # Assign a, b, and c from the list and return a new instance.
        return cls(a=a, b=b, c=c)

    def __str__(self):
        return "Triangle(a = {}, b = {}, c = {})".format(self.a, self.b, self.c)

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    # Create an object using the default constructor.
    obj1 = Triangle(1, 2, 3)
    print("Object created using __init__():", obj1)
    # Create an object using fromList() constructor.
    obj2 = Triangle.fromList([10, 20, 30])
    print("Object created using fromList():", obj2)
    # Create an object using fromString() constructor.
    obj3 = Triangle.fromString("5 10 15")
    print("Object created using fromString():", obj3)

    print(obj1.perimeter(), obj2.perimeter(), obj3.perimeter())

