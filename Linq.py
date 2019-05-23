from AnonObject import AnonObject

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "{0} is {1} years old".format(self.name,self.age)
    
    def __repr__(self):
        return self.__str__()


people=[
    Person("Mete",30),
    Person("Bati",30),
    Person("Harari",50),
    Person("Fatma",20),
    Person("Ayse",10),
    Person("Ricardo",24)
]

query=[
    #from p in people
    #where p.age>20
    #orderby p.age descending
    #new {p.name}

    #new {p.name,p.age}
    AnonObject(name=p.name,age=p.age)

    #from p in people
    for p in people

    #where p.age>25
    if p.age>25
        
]

#orderby p.age descending
query=sorted(query,key=lambda p : -p.age)

for p in query:
    print(p)