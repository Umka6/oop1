class Student:
    name = 'name'
    age = 'age'
    major = 'major'

    def people(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major

a = Student()
a.people(name=input('name:'),age=int(input('age:')),major=input('major:'))
print('name:',a.name,'age:',a.age,'major:',a.major)

b = Student()
b.people(name=input('name:'),age=int(input('age:')),major=input('major:'))
print('name:',b.name,'age:',b.age,'major:',b.major)

c = Student()
c.people(name=input('name:'), age=int(input('age:')),major=input('major:'))
print('name:',c.name,'age:',c.age,'major:',c.major)