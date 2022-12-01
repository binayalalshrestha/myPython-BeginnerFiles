# create a class with a class attribute a;
# create an object from it and set a directly using
# object.a = 0.
# does this change the class attribute?

class Sample:
    a = 1

obj = Sample()
obj.a = 0

print(Sample.a)