# print(7**4)

# s = "Hi there Sam!"
# a= s.split()
# print(a)

# planet = "Earth"
# diameter = 12742
# print(f"The diameter of {planet} is {diameter} kilometers.")

# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3][1][2][0])

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]['tricky'][3]['target'][3])

# def domainGet(email):
#     return email.split('@')[-1]

# print(domainGet('user@meow.com'))

# def findDog(woof):
#     return 'dog' in woof.lower().split()

# w=input("enter the senternce :")
# print(findDog(w))

# def countDog(woof):
#     count = 0
#     for word in woof.lower().split():
#         if word == 'dog':
#             count += 1
#     return count

# w=input("Enter the sentence: ")
# print(countDog(w))

from operator import truediv
from pickle import FALSE


def speeding_ticket(speed, birthday):
    
    if birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding >= 80:
        return 'Big Ticket'
    elif speeding >= 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'
    

print(speeding_ticket(80,True))