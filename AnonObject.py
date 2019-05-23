#Class Definition
class AnonObject(dict):
    __getattr__=dict.get
    __setattr__=dict.__setitem__

anon=AnonObject(id=7,registered=True)    

print(anon)


