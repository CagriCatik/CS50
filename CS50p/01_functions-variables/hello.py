# Demonstrates a function with a positional argument
print("hello, world")

# Demonstrates a function with a positional argument and a return value
name = input("What's your name? ")
print("hello,")
print(name)


# Demonstrates concatenation of strings
name = input("What's your name? ")
print("hello, " + name)


# Demonstrates a function with a positional argument and a named argument
name = input("What's your name? ")
print("hello, ", end="")
print(name)


# Demonstrates a format string
name = input("What's your name? ")
print(f"hello, {name}")


# Demonstrates str functions
name = input("What's your name? ").strip().title()
print(f"hello, {name}")


# Demonstrates str functions
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")


# Demonstrates defining a function without parameters
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)


# Demonstrates defining a function with a parameter
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)


# Demonstrates defining a function with a parameter with a default value
def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)


# Demonstrates defining a main function
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)


main()

