def my_decorator(func):
  def wrapper():
    print("Something is happening BEFORE.")
    func()
    print("Something is happening AFTER.")

  return wrapper


@my_decorator
def say_hello():
  print("Hello from function!")


say_hello()