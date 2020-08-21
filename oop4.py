class Shop:
     name = 'name'
     is_open = 'yes'
     product_list = 'list'

     def add_products(self, name, is_open, product_list):
         self.name = input('name:')
         self.is_open = True
         self.product_list = int(input('product:'))

a = Shop()
a.add_products(1,2,3)
if a.product_list > 0:
    a.is_open = True
else:
    a.is_open = False
print(a.name, a.is_open, a.product_list)

class Shop:
    product = 'apple'
    count = 1
    def buy_product(self, product, count):
        self.product = product
        self.count = count
h = ['яблоко', 'хлеб', 'чай', 'мука', 'чай', 'молоко']
have = Shop()
have.buy_product(product=input('Продукт: '), count=input('Количество: '))
if have.product in h:
   print('have')
else:
   print('sorry')

class Shop:
     product = 'apple'
     count = 1
     def add_products(self, product, count):
         self.product = input('продукты: ')
         self.count = input('количества: ')
s =[]
a = Shop()
a.add_products(1, 4)
b = Shop()
b.add_products(1, 2)
c = Shop()
c.add_products(1, 2)
s = []
g = (s.append(a.product), s.append(b.product), s.append(c.product), )
print(a.product, a.count, b.product, b.count, c.product, c.count)
print(s)







