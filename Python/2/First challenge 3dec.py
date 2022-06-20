print("Welcome to Montalvo Store")
print("insert your name")

nombre=input ()
print("Welcome", nombre)

print("What food do you want to buy?")

food1=input('item 1: ')
price1=int(input('price: '))

food2=input('item 2: ')
price2=int(input('price: '))

food3=input('item 3: ')
price3=int(input('price: '))

food4=input('item 4: ')
price4=int(input('price: '))

food5=input('item 5: ')
price5=int(input('price: '))

item1=price1
item2=price2
item3=price3
item4=price4
item5=price5
subtotal=item1+item2+item3+item4+item5
total= subtotal*0.16
print(subtotal)
print(total)

print('-----TICKET-----')
print("1.",food1,"price:",price1)
print("2.",food2,"price:",price2)
print("3.",food3,"price:",price3)
print("4.",food4,"price:",price4)
print("5.",food5,"price:",price5)
print("subtotal",subtotal)
print("total",total)
print('THANKS, COME BACK')