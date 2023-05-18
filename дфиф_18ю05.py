#1
class OddIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if N <= 1:
            raise ValueError('Значення не може бути меншим або дорівнювати 1')
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 2
        return value
l = []
l2 = []
N = 7
for i in range(1, N + 1):
    l.append(i)
for n in OddIterator(l):
    l2.append(n)
print(l2)

#2

class SquareGenerator():
    def __init__(self, data):
        self.data = data
        res = isinstance(data, list)
        if res == False:
            raise TypeError('Невідомий тип даних')
    def s(self):
        for i in self.data:
            i = i ** 2
            yield i
l = []
l1 = []
N = 5
for i in range(1, N + 1):
    l.append(i)
sg = SquareGenerator(l)
for num in sg.s():
    l1.append(num)
print(l1)

#3

lst = l
l3 = []
class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        value = self.lst[self.index]
        self.index += 1
        return value
for num in ListIterator(lst):
    l3.append(num)
print(l3)

#4

def multiply_by():
    def mult(n):
        if n == int(n):
            return n * n
        else:
            raise TypeError('Введені дані не є числовими або цілими')
    return mult
m = multiply_by()
print(m(int(input('Введіть число: '))))
print(m(int(input('Введіть число: '))))



