#class Fraction uses special methods that overload operators to perform rich comparisons betweens a and b
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator==0:
            raise ZeroDivisionError("Denominator cannot be zero")
            return
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return Fraction(n, d)

    def __truediv__(self, other):
        n = self.n * other.d
        d = self.d * other.n
        return Fraction(n, d)      


    def __str__(self):
        return "{}/{}".format(self.n, self.d)


    __repr__ = __str__

    def value(self):
        return self.n/ self.d

    def __eq__(self, compare):
        return self.value()== compare.value()

    def __lt__(self,compare):
        return self.value() < compare.value()

    def __gt__(self,compare):
        return self.value() > compare.value()

#Test case
'''
a = Fraction(1, 2)
b = Fraction(1, 3)
print(a==b)
print(a>b)
print(a<b)
a = Fraction(4, 8)
b = Fraction(2, 4)
print(a==b)
print(a>b)
print(a<b)
'''

#class Book uses special methods that will return information to the user.
class Book():
    count=0
    def __init__(self, title, author, pages):
        self.title= title
        self.author= author
        self.pages= pages
        Book.count+=1
    @classmethod

     
    def __del__(self):
       del self
       Book.count-=1

    def inventory():
        return Book.count

    def __len__(self):
        return self.pages

    def __str__(self):
        return "TITLE: {} by {}".format(self.title, self.author)

    __repr__= __str__

#test cases
'''
book1= Book("Beneath a Scarlet Sky", "Mark Sullivan", 526)
book2= Book("Love in the Time of Cholera", "Gabriel G. Marquez", 357)
book3= Book("We Were the Lucky Ones", "Georgia Hunter", 414)
print(Book.inventory())
print(book1)
print(len(book1))
del book1
print(Book.inventory())
'''