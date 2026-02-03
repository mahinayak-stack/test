class A:
    def fun(self):
        print("In class A")

class B:
    def fun(self):
        print("In class B")

class C(A, B):
    def __init__(self):
        print("Constructor C")

obj = C()

print(C.__mro__) 
print(C.mro())