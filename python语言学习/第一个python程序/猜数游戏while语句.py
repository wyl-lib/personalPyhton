number = 23
running = True

while running:
  garde = int(input("Enter an integer:"))
  

  if garde == number:
        print("Yeah,you are right.")
        running = False

  elif garde < number:
        print("No,it is little lower than number")
  else:
        print("No,it is little higher than number")
else:
  print("the while loop is over.")

print("Count over")       
