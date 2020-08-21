class Person:
    name = 'name'
    lastname = 'lastname'
    year = 'year'
    def get_age(self,name,lastname,year):
        self.name = name
        self.lastname = lastname
        self.year = year
b = Person()
b.get_age(name=input('name:'),lastname=input('lastname:'),year=int(input('year:')))
print(b.name,b.lastname,'тебе',b.year)