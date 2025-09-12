#args
def greet(*args):
    for name in args:
     print("Hello",name)

greet("Alice", "Bob", "Charlie")  

#kargs
def greet_with_kwargs(**kwargs):
   for name, age in kwargs.items():
         print(f"Hello {name}, you are {age} years old.")

greet_with_kwargs(Alice=30, Bob=25, Charlie=35)

#args and kargs
def greet_all(*args, **kwargs):
  print("Args: ",args)
  print("Kwargs: ",kwargs)

greet_all("Alice", "Bob", Alice=30, Bob=25)