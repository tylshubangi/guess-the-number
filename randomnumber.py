import random
n=random.randint(0,10)
p=1
while p<=5:
    i=int(input("enter the number: "))
    if i==n:
        print("correct answer")
        break
    elif i>n:
        print("OOPS! Wrong guess, guess something lesser")
    elif i<n:
        print("Oh no, that's a wrong guess! try something greater")
    else:
        print('invalid number')
    p=p+1
print("answer is:", n)

