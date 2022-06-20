while True:
  x=int(input("guess the number:"))
  number=10
  if(x<10):
    print("its bigger")
  if(x>10):
    print("its a smaller number")
  if (x==10):
    print("its correct")