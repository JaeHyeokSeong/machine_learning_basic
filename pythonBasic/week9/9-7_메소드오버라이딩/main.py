print("9-7 practise\n")


class A:

    def greeting(self):
        print("A class - hello world")


class B(A):

    def greeting(self):
        # super().greeting()
        print("B class - hello world")


# a = A()
# a.greeting()

b = B()
b.greeting()
