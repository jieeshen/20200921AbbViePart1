



def doit(func):
    func()


class Thing:
    def __init__(self):
        self.count = 0

    def spam(self):
        print("spam!!")

    def ham(self):
        pass

    def rex(self):
        print("in rec")
        self.count += 1
        if self.count == 10:
            return
        self.rex()

    def __call__(self):
        print("Magic call")


def hello():
    print("Hello")

def goodbye():
    print("Goodbye")

doit(hello)
doit(goodbye)
t = Thing()
doit(t.spam)
doit(t)  # t is a "callable class"
doit(Thing())

t.rex()

