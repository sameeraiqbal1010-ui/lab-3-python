class CustomError(Exception):
  pass


def check_age(age):
  if age < 18:
    raise CustomError("Age must be 18 or above.")
  print("Valid age.")


try:
  check_age(15)
except CustomError as e:
  print(f"Caught an exception: {e}")