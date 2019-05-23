def find_numbers(predicate):
    for i in range(100):
        if(predicate(i)):
            yield i
                    #n=>n%11==0
numbers=find_numbers(lambda num:num%11==0)
for n in numbers:
    print(n)
