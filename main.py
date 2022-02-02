mylist = []
numlist = 1
i = True 
while i == True: 
  x = input("What should I add to my shopping list\n")
  mylist.append(str(numlist) + ". " + x)
  numlist = numlist + 1
  Again = False 
  while Again == False: 
    answer = input("do you wanna add another item? (y/n)")
    if answer == 'y':
      i = True
      Again = True
    elif answer == 'n':
      i = False 
      Again = True 
    else:
      print("invaild answer try again!")
      Again = False


print("Shopping List")
print(*mylist, sep = "\n")





