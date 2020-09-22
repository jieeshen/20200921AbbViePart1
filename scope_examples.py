
# levels of scope:  local, nonlocal, global, builtin

x = 100  # global variable

def spam():
    y = 42  # local variable
    x = "wolverine"
    print("in spam(): x is", x)
    # print(ABC)

spam()

print("in main: x is", x)
# print("in main: y is", y)

name = 'Bob'

if name == 'Bob':
    color = 'blue'

print("color:", color)

def ham():
    name = "Louise"

    def eggs():
        name = 'Scott'
        print("Name is:", name)

    return eggs

f = ham()
f()






