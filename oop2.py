class Child:
    name = 'name'
    apple = 'apple'
    def child1(self,name,apple):
        self.name = name
        self.apple = apple

a = Child()
a.child1('Karina',3)
print(a.name,a.apple)

b = Child()
b.child1('Turat',4)
print(b.name,b.apple)

c = Child()
c.child1('Umka',5)
print(c.name,c.apple)
d = a.apple+b.apple+c.apple
print(d)