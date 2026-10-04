try:
  num = int(input("Enter a number: "))
  res = 100 / num
  print(res)
except ZeroDivisionError:
  print("Cannot divide by zero!")
except ValueError:
  print("Invalid input!")