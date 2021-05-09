class A(object):
    def __init__(self):
        print("A created")
P = A()


class B(A):
    def __init__(self):
        print(super((B), self).__init__) # Q1: How to get "A created" from parent class?
        print(self.__class__.__name__)
        print(super(B, self).__class__.__name__)