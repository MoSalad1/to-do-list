a=0
list = ['empty','empty','empty','empty','empty','empty','empty','empty','empty']
def add(list):
  item = input("What would you like to add to your list? ")
  position = int(input("What position would you like to add it to? "))
  list[position] = item
  printlist(list)

def remove(list):
  item = input("What would you like to remove from your list? ")
  list.remove(item)
  printlist(list)

def printlist(list):
  for i in list:
    print(i)
while True:
  a = input(str("Would you like to add(1), remove(2), or print(3) your list? "))
  if a == "1":
    add(list)
  elif a == "2":
    remove(list)
  elif a == "3":
    printlist(list)
  else:
    print("Invalid input")
