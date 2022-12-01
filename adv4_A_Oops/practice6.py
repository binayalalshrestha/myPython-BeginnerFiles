'''
can you change the self parameter inside a class
to something else (say 'harry')
try changing self to 'slf' or 'harry' and see the effect.
'''
class Sample:
    a = "Harry"
    def __init__(slf,name):
        slf.name = name

obj = Sample("Harry")
print(obj.name)