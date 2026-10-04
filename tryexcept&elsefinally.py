try:
  f = open("sample.txt", "r")
  data = f.read()
except FileNotFoundError:
  print("File not found.")
else:
  print("File read successfully.")
  f.close()
finally:
  print("This block always runs.")