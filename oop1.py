#class Employee:
 #   name = 'name'
  #  lastname = 'lastname'
  #  position = 'pos'
  #  salary = 'sal'

   # def get_info(self,name,lastname,position,salary):
    #    self.name = input('name:')
     #   self.lastname = input('surname:')
      #  self.position = input()
       # self.salary = int(input())
#a = Employee()
#a.get_info(12,54,6,9)
#print(a.name,a.lastname,a.position,a.salary)

class Employee:
    name = 'name'
    lastname = 'lastname'
    position = 'pos'
    salary = 'sal'

    def get_info(self,name,lastname,position,salary):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.salary = salary
a = Employee()
a.get_info(name=input('name:'),lastname=input('lastname:'),position=input('position:'),salary=int(input('salary:')))
print(a.name,a.lastname,a.position,a.salary)

